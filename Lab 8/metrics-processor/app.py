import json, sqlite3, time
from statistics import mean
from pathlib import Path

DB_PATH = "/db/metrics.db"
METRICS_PATH = "/shared/metrics.json"
TMP_BUFFER_PATH = "/tmp/buffer.json"

def read_metrics():
    try:
        with open(METRICS_PATH) as f:
            data = json.load(f)
        print("Odczytano metryki:", data)
        with open(TMP_BUFFER_PATH, "a") as buf:
            json.dump(data, buf)
            buf.write("\n")
        return data
    except Exception as e:
        print("Błąd przy odczycie metryk:", e)
        return None

def save_to_db(conn, avg_cpu, avg_ram, avg_disk, timestamp):
    try:
        print(f"Zapis do DB: {timestamp} CPU: {avg_cpu} RAM: {avg_ram} DISK: {avg_disk}")
        conn.execute(
            "INSERT INTO avg_metrics (timestamp, avg_cpu, avg_ram, avg_disk) VALUES (?, ?, ?, ?)",
            (timestamp, avg_cpu, avg_ram, avg_disk)
        )
        conn.commit()
    except Exception as e:
        print("Błąd zapisu do bazy:", e)

Path("/db").mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
conn.execute("""
CREATE TABLE IF NOT EXISTS avg_metrics (
    timestamp TEXT,
    avg_cpu INTEGER,
    avg_ram INTEGER,
    avg_disk INTEGER
)
""")
conn.commit()

buffer = []

while True:
    metric = read_metrics()
    if metric:
        buffer.append(metric)
        if len(buffer) >= 3:
            avg_cpu = mean([m["cpu"] for m in buffer])
            avg_ram = mean([m["ram"] for m in buffer])
            avg_disk = mean([m["disk"] for m in buffer])
            save_to_db(conn, avg_cpu, avg_ram, avg_disk, metric["timestamp"])
            buffer = []
    time.sleep(10)
