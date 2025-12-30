import json
import random
import time
from datetime import datetime

# File to store streaming events
log_file = "src/landing/streaming/user_events.log"

# Sample event types
event_types = ["page_view", "click", "add_to_cart", "purchase"]

# Sample devices
devices = ["mobile", "desktop", "tablet"]

# Sample locations
locations = ["USA", "India", "UK", "Germany", "Canada"]

# Function to generate a random user event
def generate_event():
    event = {
        "event_id": str(random.randint(1000000, 9999999)),
        "user_id": str(random.randint(1, 1000)),
        "event_type": random.choice(event_types),
        "product_id": str(random.randint(1, 500)),
        "timestamp": datetime.utcnow().isoformat(),
        "device_type": random.choice(devices),
        "location": random.choice(locations),
        "session_id": str(random.randint(10000, 99999))
    }
    return event

# Streaming simulation: generate an event every 2 seconds
while True:
    event = generate_event()
    with open(log_file, "a") as f:
        f.write(json.dumps(event) + "\n")
    print(f"Generated event: {event['event_id']}")
    time.sleep(2)  # Adjust speed if needed
