def get_repo_tool():
    return {
        "type": "function",
        "function": {
            "name": "get_repository_health",
            "description": (
                "Retrieve GitHub repository metadata "
                "and latest commit information to "
                "assess maintenance activity."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "owner": {
                        "type": "string",
                        "description": "GitHub repository owner"
                    },
                    "repo": {
                        "type": "string",
                        "description": "GitHub repository name"
                    }
                },
                "required": ["owner", "repo"],
                "additionalProperties": False
            }
        }
    }