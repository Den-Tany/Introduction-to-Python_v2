import math
def square(num):
    return math.ceil(num * num)
while True:
    try:
        length=input("Введите длину стороны квадрата ")
        if ',' in length and '.' not in length:
            length=float(length.replace(',','.'))
        else:
            length=float(length)
        break
    except ValueError:
        print("Пожалуйста, введите число.")
print(f"Площадь квадрата {square(length)}")