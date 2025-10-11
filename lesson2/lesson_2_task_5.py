import math
def month_to_season(month): 
    if month == 12 or month>=1 and month<=2:        
        print("Зима")
    elif month>=3 and month<=5:        
        print("Весна")
    elif month>=6 and month<=8:        
        print("Лето")
    elif month>=9 and month<=11:        
        print("Осень")
while True:
    try:
        month=int(input("Введите номер месяца "))
        if month>12 or month<1:
            raise ValueError
        month_to_season(month)
        break
    except ValueError:
        print("Месяца с таким номером не существует")

