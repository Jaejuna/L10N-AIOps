import openai
import os
from dotenv import load_dotenv

load_dotenv() 

token = os.getenv('GPT_API')

if not token:
    raise ValueError("API token not found. Please check your .env file.")

openai.api_key = token

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

print(response.choices[0].message['content'])
