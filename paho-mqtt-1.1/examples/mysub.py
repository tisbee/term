import sys
try:
    import paho.mqtt.client as mqtt
except ImportError:
    # This part is only required to run the example from within the examples
    # directory when the module itself is not installed.
    #
    # If you have the module installed, just use "import paho.mqtt.client"
    import os
    import inspect
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import paho.mqtt.client as mqtt

def on_message(mqttc, obj, msg):
    print("topic: " + msg.topic + ", payload: " + str(msg.payload) + ", qos: \
" + str(msg.qos) + ", retain: " + str(msg.retain))

if __name__ == '__main__':
    mqttc = mqtt.Client()

    mqttc.on_message = on_message
    mqttc.connect("test.mosquitto.org", 1883, 60)
    mqttc.subscribe("my/topic/pepper", 0)

    mqttc.loop_forever()
