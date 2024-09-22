from flask import Blueprint
from app.transactions.transactions_routes import transactions_bp

# Create a Blueprint for the transactions module
transactions_blueprint = Blueprint('transactions', __name__)

# Register the transactions routes with the blueprint
transactions_blueprint.register_blueprint(transactions_bp)

# You might include additional setup or utility functions here
# For example, setting up transaction-related services or configurations
