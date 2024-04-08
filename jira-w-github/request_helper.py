import json
import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth


class RequestHelper:
    def __init__(self):

        load_dotenv()

        self.__jira_domain = os.getenv('jira_domain')
        self.__api_token = os.getenv('jira_token')
        self.__email = os.getenv('jira_email')

        self.__base_url = f"https://{self.__jira_domain}"
        self.__auth = HTTPBasicAuth(self.__email, self.__api_token)
        self.__headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def get_request(self, endpoint): # endpoint ex: /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes"

        url = self.__base_url + endpoint
        response = requests.request(
            "GET",
            url,
            headers=self.__headers,
            auth=self.__auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    
    def post_request(self, endpoint, payload): # endpoint ex: /rest/api/3/issue
        
        url = self.__base_url + endpoint
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=self.__headers,
            auth=self.__auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
