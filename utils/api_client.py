import requests
from config.settings import BASE_URL

class APIClient:
    response = None
    response_json = None
    
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def get(self, path, params=None):
        self.response =  requests.get(f"{self.base_url}{path}", params=params)
        self.response_json = self.response.json()
        assert self.response.status_code == 200
        
    def post(self, path, data=None):
        self.response = requests.post(f"{self.base_url}{path}", json=data)
        self.response_json = self.response.json()
        

    def put(self, path, data=None):
        return requests.put(f"{self.base_url}{path}", json=data)

    def delete(self, path):
        return requests.delete(f"{self.base_url}{path}")

