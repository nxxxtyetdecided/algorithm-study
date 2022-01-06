n = list(input())
# 왼쪽, 오른쪽으로 나누기 위한 변수
num = int(len(n)/2)

# 왼쪽, 오른쪽 리스트에 정의
left, right = n[:num], n[num:]
sum_left, sum_right = 0, 0

# 왼쪽, 오른쪽 각각의 합
for i in range(num):
  sum_left += int(left[i])
  sum_right += int(right[i])

# 최종 출력
if sum_left == sum_right:
  print("LUCKY")
else:
  print("READY")

# 6달 전 코드
"""
# Q07 럭키 스트레이트
# 난이도 하 | 풀이 시간 20분 | 시간 제한 1초 | 메모리 제한 256MB | 기출 핵심 유형
# 풀이 시간 : 5분 소요

n = list(map(int, input()))
first = n[:int(len(n)/2)]
second = n[int(len(n)/2):]

if sum(first) == sum(second) :
  print('LUCKY')
else :
  print('READY')
"""
