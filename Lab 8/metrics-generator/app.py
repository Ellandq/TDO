import json, random, time
from datetime import datetime

FILE_PATH = "/shared/metrics.json"
LOG_PATH = "/logs/metrics-copy.json"

while True:
    metrics = {
        "timestamp": datetime.now().isoformat(),
        "cpu": random.randint(0, 100),
        "ram": random.randint(0, 100),
        "disk": random.randint(0, 100),
    }

    with open(FILE_PATH, "w") as file:
        json.dump(metrics, file)
    with open(LOG_PATH, "a") as log:
        log.write(json.dumps(metrics) + "\n")
    time.sleep(10)