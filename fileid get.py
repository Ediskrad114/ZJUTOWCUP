import requests

encoded_id = "DSFJ3Y1d4dUxQRUZB" # 你表格链接里D开头这串
url = "https://docs.qq.com/openapi/v2/file/id/convert"
params = {
    "type": "encodedID",
    "value": encoded_id
}
res = requests.get(url, params=params)
print(res.json())
