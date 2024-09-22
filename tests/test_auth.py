import unittest
from app import create_app
from app.models import db

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_register(self):
        response = self.client.post('/auth/register', json={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'User created successfully', response.data)

    def test_login(self):
        self.client.post('/auth/register', json={'username': 'testuser', 'password': 'testpass'})
        response = self.client.post('/auth/login', json={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'token', response.data)

if __name__ == '__main__':
    unittest.main()
