from app import app
from utils.db import db
from models import Company, Warehouse

with app.app_context():
    # Create Company
    company = Company(name="Test Company")
    db.session.add(company)
    db.session.commit()

    # Create Warehouse
    warehouse = Warehouse(name="Main Warehouse", company_id=company.id)
    db.session.add(warehouse)
    db.session.commit()

    print("✅ Dummy data inserted successfully!")
    print(f"Company ID: {company.id}")
    print(f"Warehouse ID: {warehouse.id}")