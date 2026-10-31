"""Isolated, read-only Remote Radar portfolio showcase.

No access to Remote Radar production, its database, job feeds, ATS integrations,
secret storage, third-party APIs, or user accounts.
"""
from __future__ import annotations

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
ASSETS = {
    '/': ('static/index.html', 'text/html; charset=utf-8'),
    '/static/style.css': ('static/style.css', 'text/css; charset=utf-8'),
    '/static/app.js': ('static/app.js', 'text/javascript; charset=utf-8'),
}

# Fictional companies, postings, and metrics used for the portfolio demonstration.
DEMO_JOBS = [
    {'id': 'j-101', 'company': 'Northstar Cloud', 'title': 'Senior Product Designer', 'location': 'EMEA Remote', 'score': 94, 'category': 'Strong match', 'status': 'New', 'posted': 'Sample · 2 days ago', 'focus': 'B2B SaaS · Design systems', 'evidence': ['Enterprise SaaS design', 'Design-system ownership', 'End-to-end product work'], 'review': 'Confirm hiring countries on the employer site.'},
    {'id': 'j-102', 'company': 'Orbit Learning', 'title': 'Product Designer, AI Experiences', 'location': 'Worldwide Remote', 'score': 88, 'category': 'Strong match', 'status': 'Shortlisted', 'posted': 'Sample · 4 days ago', 'focus': 'AI UX · User research', 'evidence': ['Conversational interfaces', 'Research and prototyping', 'Working AI-assisted demo'], 'review': 'Confirm interview process and work authorization.'},
    {'id': 'j-103', 'company': 'Atlas Payments', 'title': 'Senior UX Designer', 'location': 'EU Only', 'score': 81, 'category': 'Review eligibility', 'status': 'Needs review', 'posted': 'Sample · 5 days ago', 'focus': 'Merchant tools · Data UX', 'evidence': ['Data-heavy dashboards', 'Admin workflows', 'Usability testing'], 'review': 'Country-limited remote role. Do not assume eligibility.'},
    {'id': 'j-104', 'company': 'Helio Systems', 'title': 'Design Engineer', 'location': 'Global Remote', 'score': 76, 'category': 'Review skills', 'status': 'Saved', 'posted': 'Sample · 1 day ago', 'focus': 'Design-to-code · React', 'evidence': ['Functional AI-assisted prototypes', 'GitHub workflow', 'Design QA'], 'review': 'Validate required production React experience.'},
    {'id': 'j-105', 'company': 'Lumen Health', 'title': 'Product Designer, Mobile', 'location': 'EMEA Remote', 'score': 73, 'category': 'Potential match', 'status': 'New', 'posted': 'Sample · 3 days ago', 'focus': 'Consumer mobile · Health', 'evidence': ['Native mobile UX', 'User-centered design', 'Mobile prototypes'], 'review': 'Check for required regulated-device experience.'},
]

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlsplit(self.path).path
        if path == '/health':
            self._send(200, b'{"ok":true,"mode":"showcase"}', 'application/json; charset=utf-8')
        elif path == '/api/jobs':
            body = json.dumps({'demo': True, 'jobs': DEMO_JOBS}, separators=(',', ':')).encode('utf-8')
            self._send(200, body, 'application/json; charset=utf-8')
        elif path in ASSETS:
            rel, mime = ASSETS[path]
            self._send(200, (ROOT / rel).read_bytes(), mime)
        else:
            self._send(404, b'Not found', 'text/plain; charset=utf-8')

    def do_POST(self):
        self._send(405, b'Demo is read-only', 'text/plain; charset=utf-8')

    def do_PUT(self):
        self.do_POST()

    def do_DELETE(self):
        self.do_POST()

    def _send(self, status: int, body: bytes, mime: str):
        self.send_response(status)
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('Cache-Control', 'no-store' if mime.startswith('application/json') else 'public, max-age=60')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args):
        # Request path can contain personal information. Do not log it.
        pass


def main():
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', '8765'))
    ThreadingHTTPServer((host, port), Handler).serve_forever()

if __name__ == '__main__':
    main()
