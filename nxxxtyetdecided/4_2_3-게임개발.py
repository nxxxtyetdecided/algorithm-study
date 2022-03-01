# 맵의 크기 입력
row, col = map(int, input().split())

# 현재 위치, 방향 입력
x, y, dir = map(int, input().split())

# 크기에 따른 맵 정보 입력
arr = []
for r in range(row):
  arr.append(list(map(int, input().split())))

# 북쪽을 기준으로 반시계 방향 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 반시계방향으로 도는 함수
def direction():
  # 북 0, 동 1, 남 2, 서 3
  global dir
  dir -= 1
  if dir == -1: # 서쪽
    dir = 3

cnt = 1 # 방문한 칸의 수!!!
turn = 0
arr[x][y] = 2

while True:
  direction()
  x = x + dx[dir]
  y = y + dy[dir]

  if arr[x][y] == 0:
    arr[x][y] = 2
    cnt += 1
    turn = 0 # 방향 초기화
  elif arr[x][y] ==1 or arr[x][y]==2:
    # 바다일 경우 - > 전진할 수 없는 경우 (0106 추가한 부분)
    x = x - dx[dir]
    y = y - dy[dir]
    turn += 1

  if turn == 4:
    x = x - dx[dir]
    y = y - dy[dir]
    if arr[x][y] == 1:
      break
    turn = 0

print(cnt)
