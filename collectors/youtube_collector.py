from googleapiclient.discovery import build
from config import YOUTUBE_API_KEY, N8N_WORKFLOW_KEYWORDS, COUNTRIES

class YouTubeCollector:
    def __init__(self):
        self.youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY) if YOUTUBE_API_KEY else None
    
    def collect(self):
        if not self.youtube:
            return []
        
        workflows = []
        for country in COUNTRIES:
            for keyword in N8N_WORKFLOW_KEYWORDS[:15]:
                query = f"n8n {keyword} workflow"
                try:
                    search_response = self.youtube.search().list(
                        q=query,
                        part='id,snippet',
                        maxResults=5,
                        type='video',
                        regionCode=country,
                        relevanceLanguage='en'
                    ).execute()
                    
                    for item in search_response.get('items', []):
                        if 'videoId' not in item.get('id', {}):
                            continue
                        video_id = item['id']['videoId']
                        stats = self.youtube.videos().list(
                            part='statistics,snippet',
                            id=video_id
                        ).execute()
                        
                        if stats['items']:
                            video = stats['items'][0]
                            views = int(video['statistics'].get('viewCount', 0))
                            likes = int(video['statistics'].get('likeCount', 0))
                            comments = int(video['statistics'].get('commentCount', 0))
                            
                            if views > 0:
                                workflows.append({
                                    "workflow": video['snippet']['title'],
                                    "platform": "YouTube",
                                    "popularity_metrics": {
                                        "views": views,
                                        "likes": likes,
                                        "comments": comments,
                                        "like_to_view_ratio": round(likes / views, 4),
                                        "comment_to_view_ratio": round(comments / views, 4)
                                    },
                                    "country": country,
                                    "url": f"https://youtube.com/watch?v={video_id}"
                                })
                except Exception as e:
                    print(f"YouTube error for {query} in {country}: {e}")
        
        return workflows