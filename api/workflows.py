from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        data = {
            "workflows": [
                {
                    "workflow": "Build a Whatsapp AI Agent for appointment handling",
                    "platform": "YouTube",
                    "popularity_metrics": {
                        "views": 774671,
                        "likes": 20104,
                        "comments": 403,
                        "like_to_view_ratio": 0.026,
                        "comment_to_view_ratio": 0.0005
                    },
                    "country": "US"
                },
                {
                    "workflow": "Google Sheets to Slack Integration",
                    "platform": "YouTube",
                    "popularity_metrics": {
                        "views": 125000,
                        "likes": 3200,
                        "comments": 180,
                        "like_to_view_ratio": 0.026,
                        "comment_to_view_ratio": 0.0014
                    },
                    "country": "US"
                },
                {
                    "workflow": "Email Marketing Automation",
                    "platform": "Forum",
                    "popularity_metrics": {
                        "views": 8500,
                        "replies": 45,
                        "likes": 120,
                        "contributors": 12
                    },
                    "country": "IN"
                },
                {
                    "workflow": "CRM Data Sync",
                    "platform": "Google",
                    "popularity_metrics": {
                        "avg_search_interest": 75,
                        "recent_search_interest": 82,
                        "trend_change_percent": 9.3,
                        "search_volume_estimate": 15000
                    },
                    "country": "US"
                }
            ]
        }
        
        self.wfile.write(json.dumps(data).encode())