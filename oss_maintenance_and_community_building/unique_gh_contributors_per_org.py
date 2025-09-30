# SPDX-License-Identifier: CC0-1.0
"""
Calculate the total unique contributors to a GitHub organization.

Note: You'll need to generate a personal access token to run this script.
See: https://github.com/settings/personal-access-tokens

Create Virtual Environment
--------------------------
>>> python3 -m venv venv
>>> source venv/bin/activate
>>> pip install --upgrade pip
>>> pip install requests

Examples
--------
>>> python3 oss_maintenance_and_community_building/unique_gh_contributors_per_org.py
"""

import requests


def get_all_gh_org_repos(org: str, headers: dict):
    """
    Get all repositories for a GitHub organization.
    """
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/orgs/{org}/repos?per_page=100&page={page}"
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        data = resp.json()

        if not data:
            break

        repos.extend(data)
        page += 1

    return [repo["name"] for repo in repos]


def get_gh_repo_contributors(org, repo, headers):
    """
    Get all contributors for a GitHub repo.
    """
    contributors = set()
    page = 1
    while True:
        url = f"https://api.github.com/repos/{org}/{repo}/contributors?per_page=100&page={page}"
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        data = resp.json()

        if not data:
            break

        for contributor in data:
            contributors.add(contributor["login"])

        page += 1

    return contributors


def main():
    """
    Derive all contributors for a given GitHub organization by providing a GitHub access token.
    """
    github_org = input(
        "Please enter the GitHub organization to calculate contributors for: "
    )
    github_token = input("Please enter your GitHub personal access token: ")

    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json",
    }

    repos = get_all_gh_org_repos(org=github_org, headers=headers)

    all_contributors = set()
    for repo in repos:
        print(f"Fetching contributors for {repo}...")
        contributors = get_gh_repo_contributors(
            org=github_org, repo=repo, headers=headers
        )
        all_contributors.update(contributors)

    print(f"\nTotal unique contributors to {github_org}: {len(all_contributors)}")


if __name__ == "__main__":
    main()
