import base64
import json

import requests


def read_token(jsonfile="src/dcaptcha/app/tokens/test_token.json") -> str:
    """读取 test token"""
    with open(jsonfile, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data[0]["token"], "token not found in JSON file"
    return data[0]["token"]


##api 接口地址(测试接口,  注意: 请求路径是固定不变的)
API_URL = "https://dcap.xiaocai.site/api/v1/yzm/images"


headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {read_token()}",
    "Content-Type": "application/json",
}


# 1. 读取图片并转换为 base64 编码
bgfile = "docs/example/dx_area.png"
with open(bgfile, "rb") as f:
    imgbase64 = base64.b64encode(f.read()).decode()

# 2. 准备请求的 payload 和参数, 具体的参数查看相关文档
payload = {"bg": imgbase64}
params = {"imageId": 2232501090}

# 3. 发送 POST 请求
response = requests.post(API_URL, params=params, json=payload, headers=headers)
print("返回的结果:", response.json())
