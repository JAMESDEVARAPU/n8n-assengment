from data_manager import DataManager
from datetime import datetime

if __name__ == "__main__":
    print(f"Starting data collection at {datetime.utcnow().isoformat()}")
    manager = DataManager()
    data = manager.collect_all()
    print(f"Completed: {data['total_workflows']} workflows collected")
