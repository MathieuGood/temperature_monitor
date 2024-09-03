# Switchbot Temperature Logger

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## Getting started

Clone the repo and navigate to the folder

```bash
git clone https://github.com/MathieuGood/temperature_monitor.git
cd temperature_monitor
```

Create a virtual environment and activate it

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Run the script

```bash
flask --app main run --port=5099
```

## Create a docker container to run the app on a Synology NAS

Build the docker image

```bash
docker buildx build --platform linux/amd64 -t temp-monitor:latest .
```

And save it as a tar file

```bash
docker save -o temp-monitor-image.tar temp-monitor
```
