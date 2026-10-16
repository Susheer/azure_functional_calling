from src.get_repository_health import get_repository_health
from openai import OpenAI
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
import os
load_dotenv("local.env")
az_api_key = os.getenv("API_key")
az_version = os.getenv('az_version')
endpoint = os.getenv('endpoint')
deployment_name=os.getenv('Deployment_name')


token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

response = client.responses.create(
    model=deployment_name,
    input="What is the capital of France?",
)
# testing if connection is working
print(f"answer: {response.output[0]}")


try:
    #result = get_repository_health('susheer','electron-printer')
    #print(result)
    pass
except:
    print("No Internet: Please check internet connection")



