from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA = {
    "last_updated": "2025-12-19T10:00:00",
    "total_workflows": 10,
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

@app.get("/")
def root():
    return {"message": "n8n Workflow Popularity API", "status": "live"}

@app.get("/workflows")
def get_workflows():
    return {"workflows": DATA.get('workflows', [])}

@app.get("/stats")
def get_stats():
    workflows = DATA.get('workflows', [])
    platforms = {}
    countries = {}
    for w in workflows:
        platform = w.get('platform', 'Unknown')
        country = w.get('country', 'Unknown')
        platforms[platform] = platforms.get(platform, 0) + 1
        countries[country] = countries.get(country, 0) + 1
    
    return {
        "total_workflows": len(workflows),
        "by_platform": platforms,
        "by_country": countries
    }

# Vercel handler
def handler(request):
    return app(request)