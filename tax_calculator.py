def tax_calculation(monthly_payment):
    yearly_payment = monthly_payment * 12

    if yearly_payment <= 1200:
        tariff = 6
    elif yearly_payment <= 4600:
        tariff = 15
    elif yearly_payment <= 8800:
        tariff = 24
    elif yearly_payment <= 15000:
        tariff = 35
    elif yearly_payment <= 30000:
        tariff = 38
    elif yearly_payment < 50000:
        tariff = 40
    else:
        tariff = 42

    after_tax_salary = yearly_payment - yearly_payment / 100 * tariff

    print("<연봉 계산 결과>")
    print("세율 :" , tariff)
    print("세전 연봉 :", yearly_payment)
    print("세후 연봉 :", after_tax_salary)

monthly_payment = float(input("월급을 입력하세요(만 원 단위, ex) 1억 = 10000) :"))

tax_calculation(monthly_payment)
