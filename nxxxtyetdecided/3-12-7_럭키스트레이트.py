#문제 https://www.acmicpc.net/problem/18406

# N 자릿수 입력
N = input()
length = len(N)//2

# 왼쪽 값, 오른쪽 값
left= N[:length]
right =N[length:]

# 왼쪽, 오른쪽 합
l , r =0, 0
for i in range(length):
    l += int(left[i])
    r += int(right[i])

# 값 비교
if l==r: print("LUCKY")
else: print("READY")