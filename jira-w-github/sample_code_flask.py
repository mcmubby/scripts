from flask import Flask, request
import issues

app = Flask(__name__)


@app.route('/createJira', methods=['POST'])
def createJira():

    project_key = 'GI'
    trigger_comment = '/jira'
    issue_type = '10009'

    try:
        ## Parse request payload. Ideally handle error
        data = request.get_json()

        if((data['comment']['body']).lower() == trigger_comment):
            
            return issues.create_issue(data, project_key, issue_type)
        
        else:
            return 'No action', 200
    
    ## Recommended to handle specific errors like post request to jira api failure...
    ## Rather than the blanket exception below
    except Exception as e:
        error_response = {
            'status': 'error',
            'message': str(e)
        }
        return (error_response), 500
    
@app.route('/', methods=['GET'])
def get_issue_type_meta():

    project_key = 'GI'

    try:
        return issues.get_issue_type_meta(project_key)
    
    except Exception as e:
        error_response = {
            'status': 'error',
            'message': str(e)
        }
        return (error_response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)