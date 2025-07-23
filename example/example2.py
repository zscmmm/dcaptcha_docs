import base64
import json

import requests


def read_token(jsonfile="src/dcaptcha/app/tokens/test_token.json") -> str:
    """读取 test token"""
    with open(jsonfile, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data[0]["token"], "token not found in JSON file"
    return data[0]["token"]


API_URL = "https://yzm.xiaocai.site/yzm/images"


headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {read_token()}",
    "Content-Type": "application/json",
}

bgfile = "docs/example/dx_click.png"
with open(bgfile, "rb") as f:
    imgbase64 = base64.b64encode(f.read()).decode()

payload = {"bg": imgbase64, "cw": "听埋扣"}
params = {"imageId": 2232501020}
response = requests.post(API_URL, params=params, json=payload, headers=headers)
print("返回的结果:", response.json())
