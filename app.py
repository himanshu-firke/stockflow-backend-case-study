from flask import Flask
from config import Config
from utils.db import db
from routes.product_routes import product_bp
from routes.alert_routes import alert_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

# Register routes
app.register_blueprint(product_bp)
app.register_blueprint(alert_bp)

if __name__ == "__main__":
    app.run(debug=True)