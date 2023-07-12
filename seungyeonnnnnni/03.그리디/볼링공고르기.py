n,m = map(int,input().split(" "))

arr = list(map(int,input().split(" ")))

sort = [0] * 11

for i in arr:
    sort[i] += 1

answer = 0
for i in range(1,m+1):
    n -= sort[i] # B가 선택할 수 있는 개수 
    answer += sort[i] * n # 경우의 수 계산

print(answer)