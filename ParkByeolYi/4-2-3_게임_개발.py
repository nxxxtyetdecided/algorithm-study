# 맵 세로 크기, 가로 크기
n, m = map(int, input().split())
# 캐릭터의 칸의 좌표(a, b), 바라보는 방향
a, b, d = map(int, input().split())
# 네 방향 가본 칸 or 바다
count, result = 0, 0

# 맵 입력
data = []
for _ in range(n):
  row = list(map(int, input().split()))
  data += [row]
# 캐릭터 시작 지점
data[a][b] = 2

# 북쪽, 동쪽, 남쪽, 서쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 방향 돌리기
direction = {0: 3, 3: 2, 2: 1, 1: 0}

while True:
  # 왼쪽으로 회전
  d = direction[d]

  # 한 방향으로 이동
  a += dx[d]
  b += dy[d]

  # 해당 칸이 1(바다) 혹은 2(가본 칸)이면 뒤로 다시 이동
  if data[a][b] == 1 or data[a][b] == 2:
    a -= dx[d]
    b -= dy[d]
    count += 1

  # 해당 칸이 가보지 않은 칸
  elif data[a][b] == 0:
    data[a][b] = 2
    count = 0

  # 네 방향 모두 가본 칸 혹은 바다
  if count == 4:
    # 뒤로 한 칸
    a -= dx[d]
    b -= dy[d]
    count = 0
    # 현재 칸이 1(바다)이면 종료
    if data[a][b] == 1:
      break

# 맵에서 캐릭터가 방문한 칸의 수
for i in range(n):
  for j in range(m):
    if data[i][j] == 2:
      result += 1

print(result)
