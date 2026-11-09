#калькулятор
while True:
    first=float( input("Введите первое число:"))
    op=input("Введите действие(-,+,/,*):")
    second=float( input("введите второе число:"))

    if op=="+":
        print(first+second)
    elif op=="-":
        print(first-second)
    elif op=="/":
        if second==0:
            print("ЭЙ!на ноль делить нельзя!")
        else:
            print(first/second)
    elif op=="*":
        print(first*second)
    else:
        print("Неизвестная команда")
    a=input("Выйти?")
    if a=="Да":
        print("Расчёт окончен")
        break      
