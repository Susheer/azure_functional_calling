from src.repo_health import repo_health
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



result = repo_health('susheer','electron-printer')
print(result)