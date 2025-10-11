class Smartphone:
    phoneBrand='noName'
    phoneModel='noName'
    subscriberNumber='+79'
    def __init__(self, phoneBrand, phoneModel, subscriberNumber):
        self.phoneBrand=phoneBrand
        self.phoneModel=phoneModel
        self.subscriberNumber=subscriberNumber
    
    def printCat(self):
        print (f"{self.phoneBrand} - {self.phoneModel}.{self.subscriberNumber}")
