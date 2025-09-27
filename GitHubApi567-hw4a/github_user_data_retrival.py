import requests

def get_github_user_data_retrival(user_id):

    repos_url = f"https://api.github.com/users/{user_id}/repos"
    repos_response = requests.get(repos_url)

    if repos_response.status_code != 200:
        raise Exception("Error fetching user repos data")

    repos = repos_response.json()
    results = []

    for repo in repos:
        repo_name = repo["name"]
        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commits_response = requests.get(commits_url)

        if commits_response.status_code != 200:
            raise Exception("Error fetching user data repos commits")

        commits = commits_response.json()
        commit_count = len(commits) if isinstance(commits, list) else 0

        results.append({"repo": repo_name, "commits": commit_count})

    return results


if __name__ == "__main__":
    user = input("Enter a GitHub username: ").strip()
    try:
        repos_info = get_github_user_data_retrival(user)
        if not repos_info:
            print("No repositories found for user.")
        else:
            for repo in repos_info:
                print(f"{repo['repo']} > Number of commits: {repo['commits']}")
    except Exception as e:
        print("Error:", e)