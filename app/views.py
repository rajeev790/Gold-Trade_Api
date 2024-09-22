from flask import Flask
from app.config import Config
from app.auth.auth_routes import auth_bp
from app.gold.gold_routes import gold_bp
from app.transactions.transactions_routes import transactions_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from app.models import db
    db.init_app(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(gold_bp)
    app.register_blueprint(transactions_bp)
    
    return app
