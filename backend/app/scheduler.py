import time
from datetime import datetime, timezone

if __name__ == "__main__":
    print("AI OS scheduler online")
    while True:
        print(f"scheduler heartbeat {datetime.now(timezone.utc).isoformat()}")
        time.sleep(60)
