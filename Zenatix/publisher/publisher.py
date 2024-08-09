import time
import random
import json
import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "hotel/temperature"

client = mqtt.Client()

def publish_temperature():
    while True:
# simulating the reading temperature data
        temperature = random.uniform(20.0, 30.0)  # this is simulated temperature data
        data = {
            "temperature": temperature,
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
# converting data into a JSON string before publishing
        json_data = json.dumps(data)
        
# publishing data to the MQTT topic
        client.publish(MQTT_TOPIC, json_data)
        print(f"Published: {json_data}")
        
# waiting for 60 seconds before publishing next data point
        time.sleep(60)

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

publish_temperature()
