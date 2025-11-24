import requests


class addProjekt:

    def __init__(self, basUrl, nameProjekt, result_auth):
            self.basUrl = basUrl
            apiKey = result_auth['apiKey']
            self.apiKey = apiKey
            data_projekt = {
                  'title': nameProjekt,
                  'users': {
                              result_auth['idAdmin']: 'admin'
                           }
                  }
            self.data_projekt = data_projekt

    def add_Projekt(self):
        authkey = f'Bearer {self.apiKey}'
        res = requests.post(
                            self.basUrl + 'projects',
                            headers={
                                    'Content-Type': 'application/json',
                                    'Authorization': authkey
                                    },
                            json=self.data_projekt
                            )
        return res
