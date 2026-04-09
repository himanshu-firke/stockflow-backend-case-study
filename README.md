# StockFlow Backend Case Study

## Candidate
Himanshu Firke
---

## 📄 Case Study Document

👉 **Full Detailed Solution (Google Docs):**  
[https://docs.google.com/document/d/1mzj-Fg85nNIaeOFjQtGITMyH8s1tl782_NK1pThORRA/edit?usp=sharing]

---
## Overview
This project implements a backend system for inventory management supporting multi-warehouse tracking and supplier relationships.

## Features
- Product creation API with validation
- Low stock alert system
- Multi-warehouse inventory support
- Error handling and transaction safety

## Tech Stack
- Python (Flask)
- SQLAlchemy
- SQLite

## Project Structure
app.py – main server  
models.py – database models  
routes/ – API routes  
utils/ – DB setup  

## How to Run
pip install -r requirements.txt  
python app.py  

## API Endpoints
POST /api/products  
GET /api/companies/<id>/alerts/low-stock  

## Testing
Tested using Postman with:
- Success cases
- Error handling
- Edge cases

