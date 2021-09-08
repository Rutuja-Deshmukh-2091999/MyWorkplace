p = int(input())
if p <= 100 or p >= 200:
    print("INVALID INPUT")
else:
    if not p%2 == 0:
        p = p - 1
        print(p//4)
        print(p//4)
        print(p//4)
        print((p//4)+1)
    else:
        print(p//4)
        print(p//4)
        print(p//4)
        print(p//4)
