def make_string(N, S):
    T = ''
    left = 0
    right = N - 1
    while left <= right:
        # 두 포인터가 가리키는 문자열이 동일한 경우
        if S[left] == S[right]:
            l = left
            r = right
            while S[l] == S[r] and l < r:
                l += 1
                r -= 1
            if S[l] < S[r]:
                T += S[left]
                left += 1
            else:
                T += S[right]
                right -= 1
        else:
            if S[left] < S[right]:
                T += S[left]
                left += 1
            else:
                T += S[right]
                right -= 1
    return T

# 입력
N = int(input().strip())
S = [input().strip() for _ in range(N)]

# 문자열 생성
T = make_string(N, ''.join(S))

# 80글자마다 줄 바꿈하여 출력
for i in range(0, len(T), 80):
    print(T[i:i+80])
