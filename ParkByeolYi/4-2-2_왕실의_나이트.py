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
