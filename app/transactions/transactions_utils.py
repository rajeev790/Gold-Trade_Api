import threading
from app.models import db, Transaction, User
from app.config import Config
import redis

# Initialize Redis client
redis_client = redis.StrictRedis.from_url(Config.REDIS_URL)

def process_transaction(user_id, amount, transaction_type):
    """
    Process a transaction (buy or sell) and update the user's balance.
    
    Args:
        user_id (int): The ID of the user making the transaction.
        amount (float): The amount of gold to be bought or sold.
        transaction_type (str): The type of transaction, either 'buy' or 'sell'.
        
    Returns:
        bool: True if transaction is successful, False otherwise.
    """
    # Acquire a Redis lock for transaction processing
    lock_key = f"transaction_lock_{user_id}"
    lock = redis_client.lock(lock_key, timeout=10)  # Lock for 10 seconds

    if lock.acquire(blocking=True):
        try:
            # Fetch the user
            user = User.query.get(user_id)
            if not user:
                return False

            # Perform transaction
            if transaction_type == 'buy':
                # Example calculation
                user.balance -= amount
                if user.balance < 0:
                    return False  # Insufficient balance
            elif transaction_type == 'sell':
                # Example calculation
                user.balance += amount
            else:
                return False  # Invalid transaction type

            # Create transaction record
            new_transaction = Transaction(user_id=user_id, amount=amount, type=transaction_type)
            db.session.add(new_transaction)
            db.session.commit()
            return True

        finally:
            lock.release()  # Release the lock
    return False

def get_transaction_history(user_id, page=1, per_page=10):
    """
    Get a paginated list of transactions for a user.
    
    Args:
        user_id (int): The ID of the user.
        page (int): The page number for pagination.
        per_page (int): Number of transactions per page.
        
    Returns:
        list: A list of transactions for the user.
    """
    transactions = Transaction.query.filter_by(user_id=user_id).paginate(page, per_page, False)
    return transactions.items

def validate_transaction_amount(amount):
    """
    Validate if the transaction amount is positive.
    
    Args:
        amount (float): The amount to be validated.
        
    Returns:
        bool: True if amount is valid, False otherwise.
    """
    return amount > 0
