import httpx
from typing import Union, Dict

BASE_URL = "https://api.github.com"

async def get_github_api_response(url: str) -> Dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

async def get_issues(owner: str, repo: str) -> Union[Dict, None]:
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"
    try:
        return await get_github_api_response(url)
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return None
        else:
            raise

async def get_stars_count(owner: str, repo: str) -> Union[Dict, None]:
    url = f"{BASE_URL}/repos/{owner}/{repo}"
    try:
        return await get_github_api_response(url)
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return None
        else:
            raise

async def get_user_repos_count(username: str) -> Union[Dict, None]:
    url = f"{BASE_URL}/users/{username}"
    try:
        return await get_github_api_response(url)
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return None
        else:
            raise

async def get_user(username: str) -> Union[Dict, None]:
    url = f"{BASE_URL}/users/{username}"
    try:
        return await get_github_api_response(url)
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return None
        else:
            raise

async def get_repositories(owner: str) -> Union[Dict, None]:
    url = f"{BASE_URL}/users/{owner}/repos"
    try:
        return await get_github_api_response(url)
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return None
        else:
            raise
