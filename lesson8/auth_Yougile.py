import requests


class Auth:

    def __init__(self, data, basUrl, ):
        self.data = data
        self.basUrl = basUrl

    def auth(self):
        r = requests.post(self.basUrl + 'auth/companies',
                          headers={'Content-Type': 'application/json'}, json=self.data)
        return r

    def get_Keys(self, id):
        del self.data['name']
        self.data['companyId'] = id
        res = requests.post(self.basUrl + 'auth/keys/get',
                            headers={'Content-Type': 'application/json'}, json=self.data)
        return res

    def get_List_Employees(self, apiKey):
        authkey = f'Bearer {apiKey}'
        res = requests.get(self.basUrl + 'users',
                           headers={'Content-Type': 'application/json', 'Authorization': authkey})
        return res
