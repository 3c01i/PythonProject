n = int(input())
data = [1,1]
for i in range(2,n):
    data.append(data[i-1]+data[i-2])
print(data[n-1])