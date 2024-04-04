import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import json
import os

load_dotenv()

jira_domain = os.getenv('jira_domain')
api_token = os.getenv('jira_github_token')
email = os.getenv('jira_email')

url = f"https://{jira_domain}/rest/api/3/project/search"

auth = HTTPBasicAuth(email, api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))