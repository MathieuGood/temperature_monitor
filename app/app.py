import asyncio
import aiohttp
from datetime import datetime
from flask import Flask, render_template
from app.requests import get_devices, get_devices_status, build_header

global devices_list


async def fetch_devices():
    print("Starting fetch devices")
    start = datetime.now()
    header = build_header()
    async with aiohttp.ClientSession() as session:
        devices = await get_devices(session, header)
    print(f"Time taken to fetch devices: {datetime.now() - start}")
    return devices


def create_app():
    app = Flask(__name__)

    @app.route("/")
    async def index():
        print(">>> ROUTE '/' queried")
        start = datetime.now()

        global devices_list
        header = build_header()
        async with aiohttp.ClientSession() as session:
            devices_status = await get_devices_status(session, devices_list, header)
        print(f"Time taken: {datetime.now() - start}")

        if len(devices_status) < 4:
            return "Not enough devices found.", 500

        return render_template("index.html", devices=devices_status)

    return app


app = create_app()
with app.app_context():
    devices_list = asyncio.run(fetch_devices())
