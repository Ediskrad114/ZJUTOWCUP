import requests

# =====================【必须修改这里！】=====================
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHQiOiIwZDU5MzgyYTY4OWY0NGY5OGY3NDgxMmNjNTE1YmUxMCIsInR5cCI6MSwiZXhwIjoxNzkzMjk0NDM2LjEwMzg2MywiaWF0IjoxNzkwNzAyNDM2LjEwMzg2Mywic3ViIjoiYWY1ZmQyNTU1YjliNDI0NWFiNmY0YjUwZDIwNjdkZTEifQ.SsEsu9vP0nq3W7t2q8cUGLjGoC9-7zdFevZ1CvN28rQ"
CLIENT_ID = "0d59382a689f44f98f74812cc515be10"
FILE_ID = "HRwcWxuLPEFA"
SHEET_ID = "BB08J2"
# ===========================================================

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Client-Id": CLIENT_ID,
    "Content-Type": "application/json"
}

def test_read_sheet():
    # 读取A2:A10范围，测试能不能拿到表格数据
    url = f"https://docs.qq.com/openapi/spreadsheet/v3/files/{FILE_ID}/sheets/{SHEET_ID}/values/A2:A10"
    resp = requests.get(url, headers=headers)
    print("HTTP状态码：", resp.status_code)
    print("返回原始JSON：")
    print(resp.json())

if __name__ == "__main__":
    test_read_sheet()

