def solution(s):
    answer = len(s)
    # 문장의 반 이상으로 압축할 수 없어서 /2
    for i in range(1, int(len(s)/2)+1):
        # 현재 단위로 자른 문자열을 담을 변수
        data = []
        # for문으로 data 리스트에 추가
        for j in range(i, len(s)+1, i):
            data += [s[j-i:j]]
        # 만약 현재 단위로 나누어 떨어지지 않을 경우 마지막 문자열 추가
        if len(s)%i != 0:
            data += [s[len(s)-i+(i-len(s)%i):]]

        # 현재 문자열이 몇 번 반복했는지, 현재 단위로 자른 압축 값
        now, result = 1, ""
        # 문자열 압축하는 for문
        for k in range(1, len(data)):
            # 이전과 현재가 같으면
            if data[k-1] == data[k]:
                now += 1
            # 이전과 현재가 다르면
            else:
                # 1일 경우는 필요 없으니 삭제
                if now != 1:
                    # 현재까지 반복한 횟수 추가
                    result += str(now)
                # 이전 문자열 추가
                result += data[k-1]
                # 다시 1로 정의
                now = 1
        if now != 1:
            # 현재까지 반복한 횟수 추가
            result += str(now)
        # 마지막 현재 문자열 추가
        result += data[k]
        # 압축한 문자열 중 가장 짧은 것의 길이
        answer = min(answer, len(result))
    
    return answer
