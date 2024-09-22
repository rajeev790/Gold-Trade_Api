from flask import Blueprint
from app.gold.gold_routes import gold_bp

# Create a Blueprint for the gold trading module
gold_blueprint = Blueprint('gold', __name__)

# Register the gold trading routes with the blueprint
gold_blueprint.register_blueprint(gold_bp)

# You might include additional setup or utility functions here
# For example, setting up gold price fetching services or other configurations
