# 풀지 못해서 답안 풀이를 보고 공부
def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 +1):
        compressed =""
        prev = s[:step]
        cnt = 1

        # 문자열과 비교
        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                cnt += 1
            else:
                if cnt >= 2 :
                    compressed += str(cnt) + prev
                else:
                    compressed += prev
                prev = s[i:i+step] # 다음 문자열로 초기화
                cnt = 1
        compressed += str(cnt) + prev if cnt >=2 else prev
        answer = min(answer, len(compressed))
    return answer