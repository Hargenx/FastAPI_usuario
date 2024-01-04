from fastapi import FastAPI, HTTPException
import github

app = FastAPI()

@app.get("/repositories/{owner}/{repo}/issues")
async def get_issues(owner: str, repo: str):
    issues = await github.get_issues(owner, repo)
    if issues is None:
        raise HTTPException(status_code=404, detail="Repo not found")
    return issues

@app.get("/repositories/{owner}/{repo}/stars")
async def get_stars_count(owner: str, repo: str):
    stars_count = await github.get_stars_count(owner, repo)
    if stars_count is None:
        raise HTTPException(status_code=404, detail="Repo not found")
    return {"stars_count": stars_count["stargazers_count"]}

@app.get("/users/{username}/repos/count")
async def get_user_repos_count(username: str):
    repos_count = await github.get_user_repos_count(username)
    if repos_count is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"repos_count": repos_count["public_repos"]}

@app.get("/users/{username}")
async def get_user(username: str):
    user_info = await github.get_user(username)
    if user_info is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_info

@app.get("/repositories/{owner}")
async def get_repositories(owner: str):
    repositories = await github.get_repositories(owner)
    if repositories is None:
        raise HTTPException(status_code=404, detail="User not found")
    return repositories
