# 4-2-2 왕실의 나이트
# 풀이 시간 : 16분
# 코드 리뷰 : 한 번 풀었던 문제여서 비교적 금방 풀 수 있었는데 처음 input()으로 list()에 하나씩 넣어주는 부분에서 7분을 썼다.

night = list(input())
# 딕셔너리로 알파벳 정의
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
# 아래와 같이 정의할 수도 있다.
# x = int(ord(night[0])) - int(ord('a'))
x, y = int(alphabet[night[0]])-1, int(night[1])-1
answer = 0

dx = [2, 2, 1, 1, -2, -2, -1, -1]
dy = [1, -1, 2, -2, 1, -1, 2, -2]

for i in range(8):
  nx = x + dx[i]
  ny = y + dy[i]
  # 정원 밖으로 나가지 않는 경우
  if 0 <= nx <= 7 and 0 <= ny <= 7:
    answer += 1

print(answer)
