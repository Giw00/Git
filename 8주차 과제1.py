# 햄버거 가격 입력
burger_prices = [int(input()) for _ in range(3)]

# 음료 가격 입력
drink_prices = [int(input()) for _ in range(2)]

# 가장 싼 햄버거와 음료의 가격 찾기
min_burger_price = min(burger_prices)
min_drink_price = min(drink_prices)

# 세트 메뉴 가격 계산
set_menu_price = min_burger_price + min_drink_price - 50

# 결과 출력
print(set_menu_price)