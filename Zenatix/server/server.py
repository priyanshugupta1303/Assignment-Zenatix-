from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "sensor_data.json"

def load_sensor_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return data
    else:
        return {"temperature": None, "timestamp": None}

@app.route('/sensor_data', methods=['GET'])
def get_sensor_data():
    data = load_sensor_data()
    if data["temperature"] is None:
        return jsonify({"error": "No data available"}), 404
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
