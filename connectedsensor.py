import paho.mqtt.client as mqtt
#from sense_hat import SenseHat

# Define the MQTT broker address and topic
broker_address = "127.0.0.1"
topic = "my-temp"

# Initialize the Sense HAT
#sense = SenseHat()

# MQTT callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        
        # Retrieve the temperature from the Sense HAT
        
        # Format the temperature value with "°C"
        temperature_with_unit = "temp °C"
        
        # Publish the temperature value to the MQTT topic
        client.publish(topic, temperature_with_unit)
    else:
        print(f"Connection to MQTT broker failed with code {rc}")
        client.disconnect()

def on_publish(client, userdata, mid):
    print("Message published")

# Create an MQTT client and set the callback functions
client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to the MQTT broker
client.connect(broker_address, 1883)  # 1883 is the default MQTT port

# Start the MQTT client loop
client.loop_start()

try:
    # Keep the script running until Ctrl+C is pressed
    while True:
        pass
except KeyboardInterrupt:
    print("Script terminated by user (Ctrl+C)")
    client.disconnect()
