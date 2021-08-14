def gugudan(number):
    for i in range(10):
        if i % 2 == 0:
            continue
        elif number * i > 50:
            continue
        else:
            print(number, "X", i, "=", number * i)

number = int(input("몇 단? :"))
print(number, "단")
gugudan(number)
