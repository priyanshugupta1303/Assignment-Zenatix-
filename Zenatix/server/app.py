from flask import Flask, jsonify
import json

app = Flask(__name__)

def get_last_data():
    try:
        with open("subscriber/temperature_data.json", "r") as file:
            lines = file.readlines()
            last_line = lines[-1] if lines else None
            return json.loads(last_line) if last_line else None
    except Exception as e:
        return {"error": str(e)}

@app.route('/sensor/temperature', methods=['GET'])
def get_temperature():
    data = get_last_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
