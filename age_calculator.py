Korean_age = input("한국 나이를 쓰시오 : ")
birth = input("생일이 지났으면 1, 생일이 지나지 않았으면 2를 입력하시오 : ")
American_age = int(Korean_age) - int(birth)
print("당신의 미국 나이 : ", American_age)
