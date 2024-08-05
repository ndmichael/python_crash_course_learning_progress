import requests

#Make an api call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to dictionry
response_dict = r.json()
print(*response_dict.keys(), sep="\n")

print(f"Total Repositories: {response_dict['total_count']}")
print(f"Complete result: {not response_dict['incomplete_results']}")

# Explore inforation about the repository
repo_dicts = response_dict['item']
print(f"Repository returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

for key in sorted(repo_dict.keys()):
    print(key, end="\n")