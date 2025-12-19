from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from data_manager import DataManager
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")
data_manager = DataManager()

scheduler = BackgroundScheduler()
scheduler.add_job(func=data_manager.collect_all, trigger="cron", hour=2, minute=0)
scheduler.start()

@app.get("/")
def root():
    return {
        "message": "n8n Workflow Popularity API",
        "endpoints": {
            "/workflows": "Get all workflows",
            "/workflows/platform/{platform}": "Filter by platform (YouTube, Forum, Google)",
            "/workflows/country/{country}": "Filter by country (US, IN)",
            "/refresh": "Manually trigger data collection",
            "/stats": "Get statistics"
        }
    }

@app.get("/workflows")
def get_workflows(platform: str = None, country: str = None, min_views: int = None, limit: int = None):
    data = data_manager.get_data()
    workflows = data['workflows']
    
    if platform:
        workflows = [w for w in workflows if w['platform'].lower() == platform.lower()]
    
    if country:
        workflows = [w for w in workflows if w.get('country', '').upper() == country.upper()]
    
    if min_views:
        workflows = [w for w in workflows if w.get('popularity_metrics', {}).get('views', 0) >= min_views]
    
    if limit:
        workflows = workflows[:limit]
    
    return {
        "total": len(workflows),
        "last_updated": data['last_updated'],
        "workflows": workflows
    }

@app.get("/workflows/platform/{platform}")
def get_by_platform(platform: str):
    workflows = data_manager.filter_by_platform(platform)
    return {"platform": platform, "count": len(workflows), "workflows": workflows}

@app.get("/workflows/country/{country}")
def get_by_country(country: str):
    workflows = data_manager.filter_by_country(country.upper())
    return {"country": country.upper(), "count": len(workflows), "workflows": workflows}

@app.post("/refresh")
def refresh_data():
    data = data_manager.collect_all()
    return {"message": "Data refreshed", "total_workflows": data['total_workflows'], "timestamp": data['last_updated']}

@app.get("/stats")
def get_stats():
    data = data_manager.get_data()
    workflows = data['workflows']
    
    platforms = {}
    countries = {}
    
    for w in workflows:
        platform = w['platform']
        country = w.get('country', 'Unknown')
        platforms[platform] = platforms.get(platform, 0) + 1
        countries[country] = countries.get(country, 0) + 1
    
    return {
        "total_workflows": len(workflows),
        "last_updated": data['last_updated'],
        "by_platform": platforms,
        "by_country": countries
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002)
