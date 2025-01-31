import unittest
from flask import Flask
from app import app


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test client before each test."""
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test if home page loads successfully."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Generate Wi-Fi QR Code', response.data)

    def test_qr_code_generation(self):
        """Test QR code generation with valid data."""
        response = self.app.post('/', data={
            'ssid': 'TestWiFi',
            'password': 'TestPassword',
            'auth_type': 'WPA'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'image/png')

    def test_qr_code_generation_missing_data(self):
        """Test QR code generation with missing data."""
        response = self.app.post('/', data={
            'ssid': '',
            'password': '',
            'auth_type': 'WPA3'
        })
        self.assertEqual(response.status_code, 400)  # Expecting a bad request response


if __name__ == '__main__':
    unittest.main()
