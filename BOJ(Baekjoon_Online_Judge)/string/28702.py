for i in range(3, 0, -1):
    x = input()
    if x.isdigit():  # 숫자면 변환 후 원래 값 복원
        n = int(x) + i

print('Fizz' * (n % 3 == 0) + 'Buzz' * (n % 5 == 0) or n)
