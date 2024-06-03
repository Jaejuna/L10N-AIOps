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
    'Authorization': token
}

# GET 요청 보내기
response = requests.get(url, headers=headers)

# 응답 상태 코드 확인
print(f"Status Code: {response.status_code}")

# 응답 데이터 출력 (JSON 형식)
data = response.json()
print(data)