from app import app
from utils.db import db
from models import Sales

with app.app_context():
    sale = Sales(
        product_id=1,   # IMPORTANT: match your product ID
        quantity=10
    )
    db.session.add(sale)
    db.session.commit()

    print("✅ Sales data added!")