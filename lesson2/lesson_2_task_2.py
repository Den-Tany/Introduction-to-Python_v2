def is_year_leap(num):
    if num % 4 ==0:
        return "True"
    else:
        return "False"
    
while True:
    try:
         year=int(input("Введите год (число) "))
         break
    except ValueError:
         print("Значение года длжно быть целым числом")
print (f"год {year}: {is_year_leap(year)}")