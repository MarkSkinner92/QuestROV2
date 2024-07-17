# Protocols for the Control Scripts

Serial data will be sent OUT the serial port by publishing `serial <message>` to port 5555. a newline `/n` will be appended to each message.

Listening to incoming serial data is done by subscribing to port 5556. It will come in the form of `serial <message>`

Data going from the ROV to the GCS will be published to port 5556 like this:
`web/<subpath> <message>`

Listening to incoming data from the GCS is done by subscribing to port 5555. It will come in the form of `man/<message type> <string value>`. the message types are the keys of inputMapping in config.json

```
context = zmq.Context()

# Set up subscriber
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://127.0.0.1:5555")
subscriber.setsockopt_string(zmq.SUBSCRIBE, "")

# Set up publisher
publisher = context.socket(zmq.PUB)
publisher.connect("tcp://127.0.0.1:5556")
```