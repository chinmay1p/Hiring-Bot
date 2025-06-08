import json
from datetime import datetime
import os

def save_data(context):
    data = {
        "timestamp": str(datetime.now()),
        "conversation": context
    }

    os.makedirs("data", exist_ok=True)
    with open("data/candidates.json", "a") as f:
        f.write(json.dumps(data) + "\n")
