import requests
import redis
from app.config import Config

# Initialize Redis client
redis_client = redis.StrictRedis.from_url(Config.REDIS_URL)

def fetch_gold_price():
    """
    Fetch the current gold price from a public API and cache it in Redis.
    
    Returns:
        float: The current price of gold per gram.
    """
    api_url = 'https://api.example.com/gold-price'  # Replace with actual API endpoint
    cache_key = 'gold_price'
    cached_price = redis_client.get(cache_key)

    if cached_price:
        return float(cached_price)

    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    price = response.json().get('price_per_gram')
    if price is not None:
        # Cache the price in Redis with a TTL of 5 minutes (300 seconds)
        redis_client.setex(cache_key, 300, price)
        return float(price)

    raise ValueError("Gold price not found in API response")

def convert_grams_to_currency(grams, price_per_gram):
    """
    Convert the amount of gold from grams to currency based on the current price.

    Args:
        grams (float): The amount of gold in grams.
        price_per_gram (float): The current price of gold per gram.

    Returns:
        float: The equivalent amount in currency.
    """
    return grams * price_per_gram

def convert_currency_to_grams(currency, price_per_gram):
    """
    Convert an amount of currency to gold in grams based on the current price.

    Args:
        currency (float): The amount of currency.
        price_per_gram (float): The current price of gold per gram.

    Returns:
        float: The equivalent amount of gold in grams.
    """
    if price_per_gram == 0:
        raise ValueError("Price per gram cannot be zero")
    return currency / price_per_gram
