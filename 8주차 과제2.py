# 10개의 숫자 입력받기
numbers = [int(input()) for _ in range(10)]

# 42로 나눈 나머지 계산
remainders = [num % 42 for num in numbers]

# 서로 다른 나머지의 개수를 계산
unique_remainders = len(set(remainders))

# 결과 출력
print(unique_remainders)