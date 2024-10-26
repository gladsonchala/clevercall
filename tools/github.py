import requests
from langchain.tools import tool

@tool
def get_github_user(username: str) -> dict:
    """Fetches publicly available information about a GitHub user."""
    try:
        github_response = requests.get(f"https://api.github.com/users/{username}")
        if github_response.status_code == 200:
            return github_response.json()
        else:
            return {"error": f"GitHub user not found, status code: {github_response.status_code}"}
    except Exception as e:
        return {"error": f"Exception fetching GitHub user data: {e}"}
