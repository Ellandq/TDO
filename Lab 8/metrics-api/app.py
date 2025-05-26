from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB_PATH = "/data/metrics.db"

@app.route("/metrics")
def get_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute("SELECT * FROM avg_metrics ORDER BY timestamp DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([
        {"timestamp": r[0], "avg_cpu": r[1], "avg_ram": r[2], "avg_disk": r[3]}
        for r in rows
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
