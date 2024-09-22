from flask import Blueprint
from app.auth.auth_routes import auth_bp
from app.auth.auth_utils import jwt_required

# Create a Blueprint for the authentication module
auth_blueprint = Blueprint('auth', __name__)

# Register the authentication routes with the blueprint
auth_blueprint.register_blueprint(auth_bp)

# You might include additional setup or utility functions here
# e.g., setup JWT or other auth-related configurations
