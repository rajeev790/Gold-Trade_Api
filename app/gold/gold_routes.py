from flask import Blueprint, request, jsonify
import requests
import redis
from app.config import Config
from app.auth.auth_utils import token_required
from app.models import User, db

gold_bp = Blueprint('gold', __name__)
redis_client = redis.StrictRedis.from_url(Config.REDIS_URL)

@gold_bp.route('/gold/price', methods=['GET'])
@token_required
def get_price():
    price = redis_client.get('gold_price')
    if price:
        return jsonify({'price': price.decode('utf-8')}), 200
    response = requests.get('https://api.example.com/gold_price')
    price = response.json().get('price')
    redis_client.setex('gold_price', 300, price)  # Cache for 5 minutes
    return jsonify({'price': price}), 200

@gold_bp.route('/gold/buy', methods=['POST'])
@token_required
def buy_gold():
    data = request.get_json()
    amount = data.get('amount')
    # Handle buying logic (e.g., update user balance, create transaction)
    # Example:
    # user = get_current_user()
    # process_transaction(user, amount, 'buy')
    return jsonify({'message': 'Gold purchased successfully'}), 200

@gold_bp.route('/gold/sell', methods=['POST'])
@token_required
def sell_gold():
    data = request.get_json()
    amount = data.get('amount')
    # Handle selling logic (e.g., update user balance, create transaction)
    return jsonify({'message': 'Gold sold successfully'}), 200
