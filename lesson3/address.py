class Address:
    zip_code: str='0' #индекс
    city: str='noName' #город
    street: str='noName' #город
    building: str='noName' #дом
    apartment: str='noName' #квартира

    def __init__(self, zip_code, city, street, building, apartment):
        self.zip_code=zip_code
        self.city=city
        self.street=street
        self.building=building
        self.apartment=apartment
    def address(self):
        return (f"{self.zip_code}, {self.city}, {self.street}, {self.building} - {self.apartment}")