from app import app
from utils.db import db
from models import Product, Inventory, Sales

with app.app_context():
    p = Product.query.first()
    
    # Force correct values
    p.company_id = 1
    p.threshold = 10
    
    inv = Inventory.query.filter_by(product_id=p.id).first()
    inv.quantity = 5

    sale = Sales(product_id=p.id, quantity=10)
    
    db.session.add(sale)
    db.session.commit()

    print("✅ Forced test data ready!")