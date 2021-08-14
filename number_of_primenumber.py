#입력받은 숫자 2개 사이의 소수 개수를 출력하는 프로그램
num1 = int(input("첫 번 째 수를 입력하세요 :"))
num2 = int(input("두 번 째 수를 입력하세요 :"))

prime_number = 0
num = 0
for i in range(num1, num2+1): #i의 범위를 num1 ~ num2 까지로 설정
    num = 0 #num을 0으로 초기화
    for g in range(1, i+1): #g의 범위를 1 ~ i 까지로 설정
        if i % g == 0:
            num = num + 1
    if num == 2: #소수는 자기 자신과 1로 나누었을 때 0이므로 num == 2일 때 소수
        prime_number = prime_number + 1
    else:
        continue
print("소수의 개수는", prime_number,"입니다.")
