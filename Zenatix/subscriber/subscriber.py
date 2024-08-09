import json
import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "hotel/temperature"
DATA_FILE = "sensor_data.json"
THRESHOLD = 25.0

temperature_buffer = []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def check_alarm(temperature):
    global temperature_buffer
    
    if temperature > THRESHOLD:
        temperature_buffer.append(True)
    else:
        temperature_buffer.append(False)
    
    if len(temperature_buffer) > 5:
        temperature_buffer.pop(0)
    
    if all(temperature_buffer):
        print("Alarm: Temperature has been above the threshold for 5 minutes!")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to broker")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"Raw message payload: {payload}")
    
    try:
        message = json.loads(payload)
        print(f"Decoded message: {message}")
        save_data(message)
        check_alarm(message["temperature"])
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()
