from datetime import datetime, timezone
import json
from datetime import datetime, timezone
from .github_get import github_get

def repo_health(owner:str, repo: str)->dict[str,any]:
    pairs = ((owner, "owner"),(repo, "repo"))
    is_valid = False
    for pair in pairs:
        value = pair[0]
        label = pair[1]
        is_valid = (
            bool(value) and
            value.isascii()
        )
        # check if all the chars i the value 
        # 1 - alpha numeric 
        # 2 - is allowed charcters such as _ , .  or - 
        # 3 if all above staisfied then move to next
        if is_valid is False :
            return json.dumps({"success":False, "message":"Found Invalid Owner and Repository" })
        
        if all(char.isalnum() or char in "_.-" for char in value):
            is_valid = True

    if is_valid==False:
        return json.dumps({"success":False, "message":"Invalid Owner and Repository" })
    
    repository_url = f"repos/{owner}/{repo}"        
     
    repository = github_get(repository_url)
    commits = github_get(f"{repository_url}/commits", params={"per_page":5})
    latest_commit = True
    repository_details = {
        "repository": repository["full_name"],
        "description": repository.get("description"),
        "stars": repository["stargazers_count"],
        "forks": repository["forks_count"],
        "open_issues_and_prs": repository["open_issues_count"],
        "archived": repository["archived"],
        "last_push": repository["pushed_at"]
    }

    health_report = repository_details

    if commits:
        most_recent_commit = commits[0]
        commit_details = most_recent_commit['commit']
        latest_commit = {
            "message":commit_details["message"].splitlines()[0],
            "date": commit_details["committer"]["date"],
        }

        commit_data = {
            "latest_commit": latest_commit,
            "sampled_commits": len(commits),
            "checked_at":datetime.now(timezone.utc).isoformat()
        }
        return health_report | commit_data 
    else:
        return health_report
