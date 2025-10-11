from address import Address
class Mailing:
    to_address='noAddress' #адрес доставки
    from_address='noAddress' #адрес отправления
    cost: float=0 #стоимость Р
    track: str='noTrack' #№ трекера
    def __init__(self, from_address, to_address, cost, track):
        self.to_address=to_address
        self.from_address=from_address
        self.cost=cost
        self.track=track
    def sending(self):
        return (f"Отправление {self.track} из {self.from_address} в {self.to_address}. Стоимость {self.cost} рублей")