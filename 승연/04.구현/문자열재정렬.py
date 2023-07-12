a = input()

result=list(filter(str.isalpha,a))
result.sort()
result=''.join(result)

b = (list(map(int,filter(str.isdigit,a))))
c = 0
for i in range(len(b)):
    c += b[i]

print(result+str(c))