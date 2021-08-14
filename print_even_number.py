num1 = int(input("첫 번 째 숫자를 입력하세요 :"))
num2 = int(input("두 번 째 숫자를 입력하세요 :"))

for i in range(num1, num2+1):
    if i % 2 == 0:
        print(i, "짝수")
        if i == (num1 + num2) / 2:
            print(i, "중앙값")
    else:
        continue
