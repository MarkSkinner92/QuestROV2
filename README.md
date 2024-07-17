## A Custom ROV Extension for BlueOS
The purpose of this extension is to drive a custom non-ardupilot ROV using BlueOS.

------------

**Overview:**

Most information about the file structure can be found in the BlueOS extension docs.

app.py runs a simple Flask server, which hosts a webpage on port 5000. This webpage found at /console is used as the source of an iFrame widget in Cockpit. It has a persistant websocket connection for teleoperation. 

app.py is also connected via ZeroMQ to several other python scripts inside the controlScripts directory (see controlScripts/README in  for how that works). This allows modularity, providing clean and reliable communication with the serial port, and various I2C busses.

The python programs are started by a supervisord call, which is the entrypoint of the docker container.

------------

**Developing**
Clone this repo, including it's submodules.
install all python modules listed in requirements.txt (look in dockerfile to see a quick way)
run each python script individualy, or run `supervisord -n`  to start them all (look in the config file to see which scripts will be started)

**Build & run locally with Docker**
`docker build . -t testflask`
`docker run -p 5000:5000 --privileged testflask`
`docker run -p 5000:5000 --privileged -v git  testflask`
`docker system prune` Deletes stopped/unused containers, frees up significant disk space

**Build to Docker Hub**
`docker build . -t markskinner92/questrov:latest --output type=registry` Replace destination with your own.

------------


**User Custom Settings -- For BlueOS Extension Manager**

Extension Identifier: Quest.QuestROV
Extension Name: QuestROV
Docker Image: markskinner92/questrov
Docker tag: latest

Put this in User Custom Settings:
```
{
  "ExposedPorts": {
    "5000/tcp": {},
    "9001/tcp": {}
  },
  "HostConfig": {
    "Privileged": true,
    "ExtraHosts": ["host.docker.internal:host-gateway"],
    "PortBindings": {
      "5000/tcp": [
        {
          "HostPort": "5000"
        }
      ],
      "9001/tcp": [
        {
          "HostPort": "9001"
        }
      ]
    },
    "Binds": [
      "/dev:/dev",
      "/usr/blueos/extensions/QuestROV:/QuestROV/configuration"
    ]
  }
}
```

