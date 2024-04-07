import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import json
import os
from flask import Flask

app = Flask(__name__)

load_dotenv()

jira_domain = os.getenv('jira_domain')
api_token = os.getenv('jira_github_token')
email = os.getenv('jira_email')

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = f"https://{jira_domain}/rest/api/3/issue"

    auth = HTTPBasicAuth(email, api_token)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "GI"
        },
        "issuetype": {
            "id": "10009"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)