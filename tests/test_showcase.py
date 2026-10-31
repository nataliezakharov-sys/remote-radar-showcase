"""Standard-library regression tests; no production app access required."""
import json
import sys
import threading
import unittest
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from server import Handler

class ShowcaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.httpd = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        cls.port = cls.httpd.server_address[1]
        cls.worker = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.worker.start()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.httpd.server_close()
        cls.worker.join(timeout=2)

    def call(self, method, path):
        conn=HTTPConnection('127.0.0.1', self.port, timeout=2)
        conn.request(method, path)
        resp=conn.getresponse()
        result=resp.status, dict(resp.getheaders()), resp.read()
        conn.close()
        return result

    def test_health_and_security_headers(self):
        status, headers, body = self.call('GET','/health')
        self.assertEqual(status,200)
        self.assertEqual(json.loads(body)['mode'],'showcase')
        self.assertEqual(headers.get('X-Frame-Options'),'DENY')
        self.assertIn("connect-src 'self'",headers.get('Content-Security-Policy',''))

    def test_sample_records_are_fictional(self):
        status, headers, body=self.call('GET','/api/jobs')
        self.assertEqual(status,200)
        payload=json.loads(body)
        self.assertIs(payload['demo'],True)
        self.assertGreaterEqual(len(payload['jobs']),4)
        self.assertTrue(all('Sample' in job['posted'] for job in payload['jobs']))

    def test_read_only(self):
        for method in ('POST','PUT','DELETE'):
            with self.subTest(method=method):
                self.assertEqual(self.call(method,'/api/jobs')[0],405)

    def test_path_whitelist(self):
        for path in ('/.env','/server.py','/data/copilot.sqlite3','/api/apply','/static/../server.py'):
            with self.subTest(path=path):
                self.assertEqual(self.call('GET',path)[0],404)

    def test_static_assets(self):
        for path in ('/','/static/app.js','/static/style.css'):
            with self.subTest(path=path):
                self.assertEqual(self.call('GET',path)[0],200)

if __name__=='__main__':
    unittest.main()
