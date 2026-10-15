import json
from src.get_repository_health import get_repository_health

repo_data = get_repository_health(
    owner="tiangolo",
    repo="fastapi"
)

print(json.dumps(repo_data, indent=2))