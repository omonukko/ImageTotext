import requests
import base64

url = "https://cdn.discordapp.com/attachments/1302083210427240460/1333012658059743252/captcha.png?ex=67975847&is=679606c7&hm=a4efb8bc0a08d0763f599cf2511bd758e7ebd7f641978080339d16ee9ccebfc9&"
response = requests.get(url)
if response.status_code == 200:
    imgbase64 = base64.b64encode(response.content).decode()
    api_url = "http://localhost:8011/api/ImageToText/"
    payload = {"image": f"data:image/png;base64,{imgbase64}"}
    imagetext = requests.post(api_url, json=payload)
    print(f'{imagetext.text}')
else:
    print(f"Failed to fetch image: {response.status_code}")
