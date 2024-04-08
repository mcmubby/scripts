import json
from request_helper import RequestHelper


def create_issue(data, project_key, issue_type):
    rh = RequestHelper()

    ## Jira Ticket Payload. Payload can be swapped and passed as param but below is the minimal requirement per v3.
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
            "id": issue_type
        },
        "summary": data['issue']['title'],
    },
    "update": {}
    } )
    
    return rh.post_request('/rest/api/3/issue', payload)