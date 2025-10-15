from address import Address
from mailing import Mailing

sender=Mailing((Address("06705", "Анкара", "ул. Бюль-Бюль-Оглы", "д. 5283", "кв. 0").address())
               , (Address("SW1A 0AA", "Лондон", "ул. Длинная", "д. Высокий", "кв. Клёвая").address())
               , 1000000, 2356489).sending()
print(sender)