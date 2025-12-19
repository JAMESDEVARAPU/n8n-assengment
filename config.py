import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
DISCOURSE_API_KEY = os.getenv("DISCOURSE_API_KEY")
DISCOURSE_API_USERNAME = os.getenv("DISCOURSE_API_USERNAME")
DISCOURSE_BASE_URL = "https://community.n8n.io"

N8N_WORKFLOW_KEYWORDS = [
    "gmail automation", "slack integration", "google sheets automation",
    "whatsapp automation", "notion integration", "airtable automation",
    "webhook automation", "email automation", "crm automation",
    "social media automation", "data sync", "api integration",
    "calendar automation", "task automation", "lead generation",
    "customer onboarding", "invoice automation", "report generation",
    "backup automation", "notification system", "form automation",
    "database sync", "file management", "chatbot automation",
    "analytics automation", "marketing automation", "sales automation",
    "support ticket automation", "inventory management", "payment automation"
]

COUNTRIES = ["US", "IN"]
