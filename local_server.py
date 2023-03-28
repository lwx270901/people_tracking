import paho.mqtt.client as mqtt

# Define callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker!")
        client.subscribe("authentication")
        client.subscribe("in")
        client.subscribe("out")
        client.subscribe("total")
    else:
        print("Failed to connect to MQTT broker.")

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

    if msg.topic == "Authentication":
        print(f"Name: {msg.payload.decode()}")
    elif msg.topic == "total":
        print(f"total:   {msg.payload.decode()}")
    elif msg.topic == "in":
        print(f"in:   {msg.payload.decode()}")
    elif msg.topic == "out":
        print(f"out: {msg.payload.decode()}")




# Create MQTT client object
client = mqtt.Client()

# Set callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect("localhost")

# Start the MQTT client loop to listen for incoming messages
client.loop_forever()

