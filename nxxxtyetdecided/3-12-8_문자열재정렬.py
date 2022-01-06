# 문자열 입력
N = input()

s = [] #알파벳 담을 리스트
sum = 0 # 숫자 합계
for n in N:
    if n.isalpha(): # n이 알파벳이면
        s.append(n)
    else: #n이 숫자면
        sum += int(n)

for a in sorted(s): # 오름차순으로 정렬된 문자열 s
    print(a, end="")

if sum!=0 : print(sum) # 0이면 출력되지 않음
