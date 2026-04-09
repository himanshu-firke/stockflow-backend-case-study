from flask import Blueprint, request
from utils.db import db
from models import Product, Inventory
from decimal import Decimal

product_bp = Blueprint('product', __name__)

@product_bp.route('/api/products', methods=['POST'])
def create_product():
    data = request.json

    required_fields = ['name', 'sku', 'price']
    for field in required_fields:
        if field not in data:
            return {"error": f"{field} is required"}, 400

    try:
        existing = Product.query.filter_by(sku=data['sku']).first()
        if existing:
            return {"error": "SKU already exists"}, 400

        product = Product(
            name=data['name'],
            sku=data['sku'],
            price=Decimal(str(data['price'])),
            company_id=1  # dummy for testing
        )

        db.session.add(product)
        db.session.flush()

        if 'warehouse_id' in data and 'initial_quantity' in data:
            inventory = Inventory(
                product_id=product.id,
                warehouse_id=data['warehouse_id'],
                quantity=data['initial_quantity']
            )
            db.session.add(inventory)

        db.session.commit()

        return {"message": "Product created", "product_id": product.id}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500