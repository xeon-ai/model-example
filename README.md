# Welcome!
This is a template repository that hosts a basic computer vision model, discoverable on [xeon](https://xeon.fun). It comes with a basic python package that you can use to manage your model as well as its dataset. We have created a simple guide on how to create and publish your own models with this template below.

Before you start, make sure you have Python installed. You can install Python for your system [here](https://www.python.org/downloads/). Also, you need to install this project's dependencies. You can do this by running the following command in the root directory of this project:
```console
pip install -r requirements.txt
```

## Initializing a Project
To get started, you need to initialize a new project with the `init` command line argument. You will be prompted to answer a few questions regarding your project:
```console
> python cli.py init
Project name: Counter Blox
Project description: A yolov8 object detection model trained to identify character models in Roblox's popular Counter Blox game.
Author: xeon
---
Pretrained model [yolov8n]:
Path to dataset [dataset/]: https://universe.roboflow.com/xeon/counter-blox-640x640/dataset/8

Installing dataset...
loading Roboflow workspace...
loading Roboflow project...
Dependency ultralytics==8.0.134 is required but found version=8.0.203, to fix: `pip install ultralytics==8.0.134`
Downloading Dataset Version Zip in ./dataset/ to yolov8:: 100%|███████████████████████| 77922/77922 [00:03<00:00, 21433.96it/s]

Extracting Dataset Version Zip to ./dataset/ in yolov8:: 100%|█████████████████████| 3332/3332 [00:01<00:00, 2152.23it/s]
```
In this case we are using a public dataset hosted on Roboflow. It is highly recommended that you use a Roboflow dataset as this installation guide is designed around it. There are also tons of perks when it comes to using Roboflow datasets in your pojects. You can learn more about Roboflow on their [website](https://roboflow.com).
