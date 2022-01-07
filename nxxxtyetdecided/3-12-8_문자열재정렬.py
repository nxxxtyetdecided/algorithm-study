# 문자열 입력
N, s, sum = input(), [], 0

for n in N:
    # 알파벳이면 리스트에 추가
    if n.isalpha(): s.append(n)

    # 숫자면 더하기
    else: sum += int(n)

#오름차순으로 정렬
for a in sorted(s): print(a, end="")

#0이 아니면 문자 뒤에 숫자 이어서 출력
if sum!=0 : print(sum)
