import hashlib
import hmac
import base64
import time
import uuid
import asyncio
from datetime import datetime
from config import Config


def build_header(
    secret=Config.SECRET_KEY,
    token=Config.TOKEN,
):
    header = {}
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = "{}{}{}".format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, "utf-8")
    secret = bytes(secret, "utf-8")
    sign = base64.b64encode(
        hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest()
    )
    header["Authorization"] = token
    header["Content-Type"] = "application/json"
    header["charset"] = "utf8"
    header["t"] = str(t)
    header["sign"] = str(sign, "utf-8")
    header["nonce"] = str(nonce)
    return header


async def switchbot_request(session, url, header):
    async with session.get(url, headers=header, ssl=False) as response:
        print("Request sent to ", url)
        if response.status == 200:
            return await response.json()
        else:
            print(f"Error: {response.status}")
            response_message = (
                (await response.text())
                .replace("{", "")
                .replace("}", "")
                .replace('"', "")
            )
            print(f"Error:{response.status} {response_message}")
            return await switchbot_request(session, url, header)


async def get_devices(session, header) -> list[dict[str, str]]:
    device_list_url = "https://api.switch-bot.com/v1.0/devices"
    response_devices: dict = await switchbot_request(session, device_list_url, header)
    return [
        {"deviceName": device["deviceName"], "deviceId": device["deviceId"]}
        for device in response_devices["body"]["deviceList"]
    ]


async def get_devices_status(session, devices, header):
    timestamp = datetime.now()
    print(f"\n{timestamp}")
    tasks = []
    for device in devices:
        device_status_url = (
            f"https://api.switch-bot.com/v1.1/devices/{device["deviceId"]}/status/"
        )
        tasks.append(switchbot_request(session, device_status_url, header))

    responses = await asyncio.gather(*tasks)

    for n, response in enumerate(responses):
        devices[n]["temperature"] = response["body"]["temperature"]
        devices[n]["humidity"] = response["body"]["humidity"]
        print(devices[n]["deviceName"], "%  ", devices[n]["temperature"], "° ", devices[n]["humidity"])

    return devices
