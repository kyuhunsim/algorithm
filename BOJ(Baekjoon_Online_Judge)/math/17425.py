def sum_of_divisors(x):
    sum_divisors = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            sum_divisors += i
            if i != x // i:
                sum_divisors += x // i
    return sum_divisors

def precompute_sums(max_n):
    sum_of_division_list = [0] * (max_n + 1)
    cumulative_sum = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        for j in range(i, max_n + 1, i):
            sum_of_division_list[j] += i
    
    for i in range(1, max_n + 1):
        cumulative_sum[i] = cumulative_sum[i - 1] + sum_of_division_list[i]
    
    return cumulative_sum

import sys
input = sys.stdin.read
data = input().split()

T = int(data[0])
test_cases = [int(data[i]) for i in range(1, T + 1)]
max_test_case = max(test_cases)

# 최대 테스트 케이스 값까지 미리 계산
cumulative_sum = precompute_sums(max_test_case)

# 결과 출력
results = [str(cumulative_sum[n]) for n in test_cases]
print("\n".join(results))
