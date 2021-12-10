T = int(input())
for _ in range(T):
    N = int(input())
    Boxes = list(map(int,input().split()))
    A = 0
    B = 0
    for i in range(N):
        if (A%2) == 0:
            A += Boxes[i]
        else:
            B += Boxes[i]
    if A > B:
        print(A)
    else:
        print(B)


