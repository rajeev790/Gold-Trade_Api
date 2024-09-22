import unittest
from app import create_app
from app.models import db

class TransactionsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_transaction_history(self):
        response = self.client.get('/transactions/history')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
