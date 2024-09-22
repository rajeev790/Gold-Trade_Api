import unittest
from app import create_app
from app.models import db

class GoldTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_get_price(self):
        response = self.client.get('/gold/price')
        self.assertEqual(response.status_code, 200)

    def test_buy_gold(self):
        response = self.client.post('/gold/buy', json={'amount': 10})
        self.assertEqual(response.status_code, 200)

    def test_sell_gold(self):
        response = self.client.post('/gold/sell', json={'amount': 5})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
