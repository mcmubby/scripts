import json
from flask import Flask, request
from request_helper import RequestHelper

app = Flask(__name__)

project_key = 'GI'
trigger_comment = '/jira'
issue_type = '10009'


@app.route('/createJira', methods=['POST'])
def createJira():

    try:
        ## Parse request payload. Ideally handle error
        data = request.get_json()

        if((data['comment']['body']).lower() == trigger_comment):
            
            rh = RequestHelper()

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
                    "id": issue_type
                },
                "summary": data['issue']['title'],
            },
            "update": {}
            } )


            return rh.post_request('/rest/api/3/issue', payload)
        
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