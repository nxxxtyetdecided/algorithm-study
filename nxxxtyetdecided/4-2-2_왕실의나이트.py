# 4-2-2 왕실의 나이트
position = input() # 나이트 위치
col = ord(position[0]) - 96 # 알파벳
row = int(position[1])      # 숫자

# 움직일 수 있는 모든 경우의 수
directions = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]
num = 0

for d in directions:
    c = col + d[1]
    r = row + d[0]
    if (1<=c<=8) and (1<=r<=8): # 체스판 범위 안이라면
        num +=1
print(num)