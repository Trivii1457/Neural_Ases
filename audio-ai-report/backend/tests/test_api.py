from flask import Flask, request, jsonify
import unittest

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    def test_generate_report(self):
        response = self.client.post('/api/reports/generate', json={'audio': 'test_audio.wav'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('pdf_url', response.json)

    def test_download_pdf(self):
        response = self.client.get('/api/reports/download/test_report.pdf')
        self.assertEqual(response.status_code, 200)

    def test_generate_report_no_audio(self):
        response = self.client.post('/api/reports/generate', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()