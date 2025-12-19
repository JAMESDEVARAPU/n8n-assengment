import json
from datetime import datetime
from pathlib import Path
from collectors.youtube_collector import YouTubeCollector
from collectors.forum_collector import ForumCollector
from collectors.trends_collector import TrendsCollector

class DataManager:
    def __init__(self):
        self.data_file = Path("workflows_data.json")
        self.collectors = {
            'youtube': YouTubeCollector(),
            'forum': ForumCollector(),
            'trends': TrendsCollector()
        }
    
    def collect_all(self):
        all_workflows = []
        
        print("Collecting YouTube data...")
        all_workflows.extend(self.collectors['youtube'].collect())
        
        print("Collecting Forum data...")
        all_workflows.extend(self.collectors['forum'].collect())
        
        print("Collecting Google Trends data...")
        all_workflows.extend(self.collectors['trends'].collect())
        
        data = {
            "last_updated": datetime.utcnow().isoformat(),
            "total_workflows": len(all_workflows),
            "workflows": all_workflows
        }
        
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Collected {len(all_workflows)} workflows")
        return data
    
    def get_data(self):
        if not self.data_file.exists():
            return self.collect_all()
        
        with open(self.data_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def filter_by_platform(self, platform):
        data = self.get_data()
        return [w for w in data['workflows'] if w['platform'] == platform]
    
    def filter_by_country(self, country):
        data = self.get_data()
        return [w for w in data['workflows'] if w.get('country') == country]
