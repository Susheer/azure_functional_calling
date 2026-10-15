from src.get_repository_health import get_repository_health
from openai import AzureOpenAI
from dotenv import load_dotenv
import os
load_dotenv("local.env")
az_api_key = os.getenv("key")
az_version = os.getenv('az_version')
az_endpoint = os.getenv('az_endpoint')

client = AzureOpenAI(
    api_key= az_api_key,
    api_version= az_version,
    azure_endpoint= az_endpoint
)


try:
    result = get_repository_health('susheer','electron-printer')
    print(result)
except:
    print("No Internet: Please check internet connection")



