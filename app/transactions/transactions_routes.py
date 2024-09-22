from flask import Blueprint, jsonify, request
from app.auth.auth_utils import token_required
from app.models import Transaction

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/transactions/history', methods=['GET'])
@token_required
def transaction_history():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    # Example:
    # user = get_current_user()
    # transactions = Transaction.query.filter_by(user_id=user.id).paginate(page, per_page, False)
    return jsonify({'transactions': []}), 200
