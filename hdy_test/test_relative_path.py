import requests





class YourClass:
    def __init__(self):
        self.session = requests.Session()

    def send_request(self, params_dict):
        method = params_dict.pop('method', 'get').lower()
        url = params_dict.pop('url')
        headers = params_dict.pop('headers', {})

        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=params_dict if method == 'get' else None,
            data=params_dict if method == 'post' else None
        )

        return response


params_dict = {
    'method': 'get',
    'url': 'http://editor.release.codeghub.com/book/getList',
    'page': 1,
    'page_size': 10,
    'headers': {
        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbl9pZCI6NjgxNiwidXNlcklkIjoiNzAwZjhjOWMtZDk5OS00MGM4LTgwZDMtYWFlMjhiODcyZWI4IiwidXNlck5hbWUiOiJoZHkiLCJwaG9uZSI6IjE4NzI1OTE2MTI2Iiwib3JnX2lkIjoiIiwicm9sZUlkIjoyLCJhdXRob3JpdHkiOiJhdWRpdC8qIiwiaXAiOiIxMTMuMjQ5LjQ3LjEwNiIsImRldmljZSI6InBjIiwiZGV2aWNlX2lkIjoiNmM4ZGQ1NmI2MzFkODU2MGEzNGEzODA5ZWUwYmU4MzYiLCJCdWZmZXJUaW1lIjo4NjQwMCwiaXNzIjoiQ29kZUdyYXZpdHlIdWIiLCJleHAiOjE3MjU1MDU0ODAsIm5iZiI6MTcxNjk1MTg4MH0.8voWy5NaU0A5kjJtwRq3S4EQfJ1eaWIFfXtaM1jUQug',
        'Referer': 'http://release.codeghub.com/index/allScan'
    }
}

your_instance = YourClass()
response = your_instance.send_request(params_dict)
print(response.status_code)
print(response.json())
