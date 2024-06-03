import requests
import os
from dotenv import load_dotenv

load_dotenv() 

token = os.getenv('Konglish_API')
domain = os.getenv('Konglish-domain')

# 요청을 보낼 URL
url = domain+"/language/translate/targets"

# 요청 헤더
headers = {
    'Content-Type': 'application/json',
    'Authorization': token
}

# 전송할 데이터
data = {
    "message":"hi", 
    "translation":"google"
    }

# POST 요청 보내기
response = requests.post(url, headers=headers, json=data)

# 응답 상태 코드 확인
print(f"Status Code: {response.status_code}")

# 응답 데이터 출력 (JSON 형식)
response_data = response.json()
print(response_data)
