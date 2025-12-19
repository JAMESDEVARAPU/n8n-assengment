import requests
from config import DISCOURSE_BASE_URL, N8N_WORKFLOW_KEYWORDS

class ForumCollector:
    def __init__(self):
        self.base_url = DISCOURSE_BASE_URL
    
    def collect(self):
        workflows = []
        
        # Get latest topics from public JSON endpoints
        try:
            response = requests.get(f"{self.base_url}/latest.json", timeout=10)
            if response.status_code == 200:
                data = response.json()
                topics = data.get('topic_list', {}).get('topics', [])
                
                for topic in topics[:30]:
                    title = topic.get('title', '').lower()
                    # Filter for n8n workflow related topics
                    if any(keyword.split()[0] in title for keyword in N8N_WORKFLOW_KEYWORDS[:10]):
                        workflows.append({
                            "workflow": topic.get('title'),
                            "platform": "Forum",
                            "popularity_metrics": {
                                "views": topic.get('views', 0),
                                "replies": topic.get('posts_count', 1) - 1,
                                "likes": topic.get('like_count', 0),
                                "contributors": len(topic.get('posters', [])),
                                "engagement_score": topic.get('like_count', 0) + (topic.get('posts_count', 0) * 2)
                            },
                            "country": "Global",
                            "url": f"{self.base_url}/t/{topic.get('id')}"
                        })
        except Exception as e:
            print(f"Forum latest topics error: {e}")
        
        # Get top topics
        try:
            response = requests.get(f"{self.base_url}/top.json", timeout=10)
            if response.status_code == 200:
                data = response.json()
                topics = data.get('topic_list', {}).get('topics', [])
                
                for topic in topics[:20]:
                    title = topic.get('title', '').lower()
                    if any(keyword.split()[0] in title for keyword in N8N_WORKFLOW_KEYWORDS[:10]):
                        workflows.append({
                            "workflow": topic.get('title'),
                            "platform": "Forum",
                            "popularity_metrics": {
                                "views": topic.get('views', 0),
                                "replies": topic.get('posts_count', 1) - 1,
                                "likes": topic.get('like_count', 0),
                                "contributors": len(topic.get('posters', [])),
                                "engagement_score": topic.get('like_count', 0) + (topic.get('posts_count', 0) * 2)
                            },
                            "country": "Global",
                            "url": f"{self.base_url}/t/{topic.get('id')}"
                        })
        except Exception as e:
            print(f"Forum top topics error: {e}")
        
        return workflows