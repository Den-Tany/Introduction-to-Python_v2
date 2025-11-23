import requests


class changeProjekt:
    def __init__(self, basUrl, new_nameProjekt, result_auth, idProjekt):
        self.basUrl = basUrl
        apiKey = result_auth['apiKey']
        self.apiKey = apiKey
        self.new_nameProjekt = new_nameProjekt
        self.idProjekt = idProjekt

    def change_Projekt(self):
        authkey = f'Bearer {self.apiKey}'
        res = requests.put(
                            self.basUrl + 'projects/' + self.idProjekt,
                            headers={
                                    'Content-Type': 'application/json',
                                    'Authorization': authkey
                                    },
                            json={"title": self.new_nameProjekt}
                            )
        return res
