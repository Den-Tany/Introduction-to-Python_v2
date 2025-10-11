def fizz_buzz(num):
    for x in range(1, num + 1):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBizz")
        elif x % 5 == 0:
            print("Bizz")
        elif x % 3 == 0:
            print("Fizz")
        else:
            print(x)
while True:
    try:
        n=int(input("Введите целое число "))
        fizz_buzz(n)
        break
    except ValueError:
        print("Нужно ЦЕЛОЕ ЧИСЛО")