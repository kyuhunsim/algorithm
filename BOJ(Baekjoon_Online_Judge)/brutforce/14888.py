import itertools

# 입력 처리
N = int(input())
numbers = list(map(int, input().split()))
ops = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈의 개수

# 연산자 리스트 생성
operators = []
operators += ['+'] * ops[0]
operators += ['-'] * ops[1]
operators += ['*'] * ops[2]
operators += ['/'] * ops[3]

# 가능한 연산자 순열 생성
perm = set(itertools.permutations(operators))

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if a < 0:
            return -(-a // b)  # C++14의 음수 나눗셈 처리
        else:
            return a // b

# 최대값, 최소값 초기화
max_result = -float('inf')
min_result = float('inf')

# 각 순열에 대해 계산
for p in perm:
    result = numbers[0]
    for i in range(1, N):
        result = calculate(result, numbers[i], p[i - 1])
    
    max_result = max(max_result, result)
    min_result = min(min_result, result)

# 결과 출력
print(max_result)
print(min_result)
