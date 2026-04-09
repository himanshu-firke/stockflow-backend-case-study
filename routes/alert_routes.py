from flask import Blueprint
from utils.db import db
from models import Product, Inventory, Warehouse, Supplier, ProductSupplier, Sales
from datetime import datetime, timedelta
from sqlalchemy import func

alert_bp = Blueprint('alert', __name__)

@alert_bp.route('/api/companies/<int:company_id>/alerts/low-stock', methods=['GET'])
def low_stock_alerts(company_id):
    alerts = []

    products = db.session.query(Product, Inventory, Warehouse)\
        .join(Inventory, Product.id == Inventory.product_id)\
        .join(Warehouse, Warehouse.id == Inventory.warehouse_id)\
        .filter(Product.company_id == company_id)\
        .all()

    for product, inventory, warehouse in products:

        recent_sales = db.session.query(func.sum(Sales.quantity))\
            .filter(Sales.product_id == product.id)\
            .filter(Sales.created_at >= datetime.utcnow() - timedelta(days=30))\
            .scalar() or 0

        if inventory.quantity < product.threshold and recent_sales > 0:

            supplier = db.session.query(Supplier)\
                .join(ProductSupplier)\
                .filter(ProductSupplier.product_id == product.id)\
                .first()

            alerts.append({
                "product_id": product.id,
                "product_name": product.name,
                "sku": product.sku,
                "warehouse_id": warehouse.id,
                "warehouse_name": warehouse.name,
                "current_stock": inventory.quantity,
                "threshold": product.threshold,
                "supplier": {
                    "id": supplier.id if supplier else None,
                    "name": supplier.name if supplier else None,
                    "contact_email": supplier.contact_email if supplier else None
                }
            })

    return {"alerts": alerts, "total_alerts": len(alerts)}