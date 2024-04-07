# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json

load_dotenv()

jira_domain = os.getenv('jira_domain')
api_token = os.getenv('jira_github_token')
email = os.getenv('jira_email')
projectIdOrKey = 'GI'

url = f"https://{jira_domain}/rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes"

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