import jwt
from flask import request, jsonify
from app.config import Config

def token_required(f):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403
        try:
            jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        except Exception as e:
            return jsonify({'message': 'Token is invalid'}), 403
        return f(*args, **kwargs)
    return decorator
