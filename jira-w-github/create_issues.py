import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import json
import os
from flask import Flask, request

app = Flask(__name__)

load_dotenv()

jira_domain = os.getenv('jira_domain')
api_token = os.getenv('jira_github_token')
email = os.getenv('jira_email')
project_key = 'GI'
trigger_comment = '/jira'


@app.route('/createJira', methods=['POST'])
def createJira():

    try:
        ## Parse request payload. Ideally handle error
        data = request.get_json()

        if((data['comment']['body']).lower() == trigger_comment):
            ## Auth data
            url = f"https://{jira_domain}/rest/api/3/issue"

            auth = HTTPBasicAuth(email, api_token)

            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }


            ## Jira Ticket Payload
            payload = json.dumps( {
                "fields": {
                "description": {
                    "content": [
                        {
                            "content": [
                                {
                                    "text": data['issue']['body'],
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
                   "key": project_key
                },
                "issuetype": {
                    "id": "10009"
                },
                "summary": data['issue']['title'],
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
        
        else:
            return 'No action', 200
    
    ## Recommended to handle specific errors like empty request payload, post request to jira api failure...
    ## Rather than the blanket exception below
    except Exception as e:
        error_response = {
            'status': 'error',
            'message': str(e)
        }
        return (error_response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)