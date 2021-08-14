def grade_calculator(score):

    if int(score) >= 95:
        grade = "A+"
    elif int(score) >= 90:
        grade = "A"
    elif int(score) >= 85:
        grade = "B+"
    elif int(score) >= 80:
        grade = "B"
    elif int(score) >= 75:
        grade = "C+"
    elif int(score) >= 70:
        grade = "C"
    elif int(score) >= 65:
        grade = "D+"
    elif int(score) >= 60:
        grade = "D"
    else:
        grade = "F"

    print("당신의 학점은 ", grade," 입니다")


score = input("점수를 입력하세요 :")
grade_calculator(score)
