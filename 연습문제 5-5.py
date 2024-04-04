#사용자 정의 함수부
exchange_rate = 0

def set_rate(rate) :
    global exchange_rate
    exchange_rate = rate*0.01

def get_fixed_price(discount_price) :
    real_price = discount_price / (1 - exchange_rate)
    return int(real_price)

#주 프로그램
rate = int(input('할인율은? '))
set_rate(rate)

discount_A = int(input('A상품의 할인된 가격은? '))
discount_B = int(input('B상품의 할인된 가격은? '))

get_fixed_price(discount_A)
print('A 상품의 정가는', get_fixed_price(discount_A), '원')
get_fixed_price(discount_B)
print('B 상품의 정가는', get_fixed_price(discount_B), '원')
