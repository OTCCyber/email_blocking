import requests

def create_jira_issue(issue_data):
    url = 'https://otcindustrial.atlassian.net/rest/api/2/issue/'
    auth = ('', 'ATATT3xFfGF0JsZQltCtnfKt1ZXWnHTviyN-We81IMep5WSFqSAUfbm3trfCAs2objGjRolEDvepluyMUogMJ_Z7YdLqbswSWlOuO7EWIcmdyhJhOeffB4SUSw0e8RocxnaAJOQ5qLoglJTAIj4U2fdVpPg3NKZGeU-YTLdf3LdVhqiubi09ZAM=3693E509')
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=issue_data, auth=auth)
    if response.status_code == 201:
        issue_key = response.json()['key']
        return issue_key
    else:
        return None
