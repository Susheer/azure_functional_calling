import requests
import json

def github_get(path, params=None):
    url = f'https://api.github.com/{path}'
    response = requests.get(
        url=url,
        params=params,
        timeout=10,
        headers={"Accepet":"application/vnd.github+json", "UserAgent":"github-ai-learning-lab"}
                          )
    print("git hub remaining", response.headers.get("X-RateLimit-Remaining"))
    response.raise_for_status()
    return response.json()