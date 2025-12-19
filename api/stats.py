from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        data = {
            "total_workflows": 4,
            "by_platform": {
                "YouTube": 2,
                "Forum": 1,
                "Google": 1
            },
            "by_country": {
                "US": 3,
                "IN": 1
            }
        }
        
        self.wfile.write(json.dumps(data).encode())