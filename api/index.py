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

# Load existing data or use sample
try:
    with open('workflows_data.json', 'r') as f:
        DATA = json.load(f)
except:
    DATA = {
        "last_updated": "2025-12-19T10:00:00",
        "total_workflows": 222,
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
            }
        ]
    }

@app.get("/")
def root():
    return {"message": "n8n Workflow Popularity API", "status": "live"}

@app.get("/workflows")
def get_workflows():
    return DATA

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