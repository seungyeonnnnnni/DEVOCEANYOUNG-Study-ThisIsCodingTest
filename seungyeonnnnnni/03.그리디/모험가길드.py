n = int(input())

arr = list(map(int,input().split(" ")))
arr.sort(reverse=True)

cnt = 0
for i in range(len(arr)):
    if(cnt >= n):
        print(i)
        break
    cnt += arr[i]



