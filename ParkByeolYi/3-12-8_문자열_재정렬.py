s = list(input())
# 알파벳, 숫자 변수 선언
alphabet, number = [], 0

for i in s:
  # 알파벳이면 True
  if i.isalpha():
    alphabet.append(i)
  else:
    number += int(i)

# A~Z 정렬
alphabet.sort()
# 리스트를 문자열로 합치기
result = "".join(alphabet)
result += str(number)

print(result)
