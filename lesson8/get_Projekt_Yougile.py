import requests


class getProjekt:

    def __init__(self, basUrl, data_get, idProjekt):
        self.data_get = data_get
        self.basUrl = basUrl
        self.idProjekt = idProjekt
       
    
    def getProgekt(self):
        authkey = f'Bearer {self.data_get}'
        res = requests.get(self.basUrl + 'projects/' + self.idProjekt, headers={'Content-Type': 'application/json','Authorization': authkey})
        return res