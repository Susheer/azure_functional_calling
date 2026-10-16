from src.get_repository_health import get_repository_health
from openai import OpenAI
from dotenv import load_dotenv

import os
load_dotenv("local.env")
deployment_name=os.getenv('Deployment_name')

client = OpenAI(
    base_url=os.getenv('endpoint'),
    api_key= os.getenv("API_key")
)


try:
    #result = get_repository_health('susheer','electron-printer')
    #print(result)
    # testing if connection is working
    response = client.responses.create(
        model=deployment_name,
        input="What is the capital of France?",
    )
    print(f"answer: {response.output_text}")
except:
    print("No Internet: Please check internet connection")



