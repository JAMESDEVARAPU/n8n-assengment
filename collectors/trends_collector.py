from pytrends.request import TrendReq
from config import N8N_WORKFLOW_KEYWORDS, COUNTRIES
import time

class TrendsCollector:
    def __init__(self):
        self.pytrends = TrendReq(hl='en-US', tz=360)
    
    def collect(self):
        workflows = []
        country_map = {"US": "US", "IN": "IN"}
        
        for country_code in COUNTRIES:
            for keyword in N8N_WORKFLOW_KEYWORDS[:20]:
                query = f"n8n {keyword}"
                try:
                    self.pytrends.build_payload([query], timeframe='today 3-m', geo=country_map[country_code])
                    interest = self.pytrends.interest_over_time()
                    
                    if not interest.empty and query in interest.columns:
                        avg_interest = int(interest[query].mean())
                        recent_interest = int(interest[query].tail(7).mean())
                        trend_change = round(((recent_interest - avg_interest) / avg_interest * 100) if avg_interest > 0 else 0, 2)
                        
                        if avg_interest > 0:
                            workflows.append({
                                "workflow": keyword.title(),
                                "platform": "Google",
                                "popularity_metrics": {
                                    "avg_search_interest": avg_interest,
                                    "recent_search_interest": recent_interest,
                                    "trend_change_percent": trend_change,
                                    "search_volume_estimate": avg_interest * 100
                                },
                                "country": country_code,
                                "keyword": query
                            })
                    
                    time.sleep(1)
                except Exception as e:
                    print(f"Trends error for {query} in {country_code}: {e}")
                    time.sleep(2)
        
        return workflows