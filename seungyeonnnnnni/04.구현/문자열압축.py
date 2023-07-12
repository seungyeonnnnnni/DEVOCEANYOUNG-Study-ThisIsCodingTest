# programmers

# 문자열의 절반에서 테스트케이스를 나누며 (tmp)

def main():
    print(solution())

def solution(s):
    answer = 10000
    for n in range(1,len(s)//2+2):
        res = ''
        cnt = 1
        tmp = s[:n]

        for i in range(n,len(s)+n ,n):
            if tmp == s[i:i+n]:
                cnt +=1
            else:
                if cnt == 1:
                    res += tmp
                else:
                    res += str(cnt) + tmp
                tmp = s[i:i+n]
                cnt = 1
        answer = min(answer,len(res))
    return answer
    
if __name__ == "__main__":
    main()