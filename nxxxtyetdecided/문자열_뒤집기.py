# 백준 뒤집기
import sys

# 0과 1로 이루어진 문자열, rstrip()으로 /n 제거
arr = sys.stdin.readline().rstrip()

arr0 = 0
arr1 = 0

if arr[0] == "0":
    arr0 += 1
else:
    arr1 += 1

# 첫 번째 원소부터
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        # 0에서 1로 바뀌는 순간
        if arr[i] == "0":
            arr0 += 1
        # 1에서 0으로 바뀌는 순간
        else:
            arr1 += 1

print(min(arr0, arr1))
