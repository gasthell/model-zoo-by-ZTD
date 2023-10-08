import json
import requests
import io
import base64
from PIL import Image

url = "http://127.0.0.1:7860"

payload = {
    "prompt": "black bear, white background. an elegant, timeless, youthful logo",
    "negative_prompt": "text, realistic",
    "sampler_index": "DPM++ 2M Karras",
    "batch_size": 5,
    "cfg_scale": 8,
    "height": 512,
    "width": 512,
    "steps": 50,
    "seed": -1,
}

response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

r = response.json()
for i in range(5):
    image = Image.open(io.BytesIO(base64.b64decode(r['images'][i])))
    image.save(str(i)+'output.png')