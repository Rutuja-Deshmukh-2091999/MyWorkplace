def productsum(N,A):
    count = 0
    i = 0
    while i < len(A)-1:
        if (A[i] + (A[i+1])) == (A[i] * (A[i+1])):
            count += 1
        i += 1
    print(count)

N = int(input())
A = []

temp = input().split()
for i in range(N):
    A.append(int(temp[i]))

productsum(N,A)