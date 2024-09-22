from flask import Flask
from app.auth import auth_blueprint

def create_app():
    app = Flask(__name__)
    
    # Register the authentication blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    # Other setup code...

    return app
