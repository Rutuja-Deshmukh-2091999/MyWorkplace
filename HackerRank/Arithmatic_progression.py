# Arithmatic Progression a + a + d + a + 2d + a + 3d

def sumofap(a,d,n):
    sum = 0;
    i = 0 ;
    while i < n:
        sum = sum + a
        a = a + d
        i = i + 1
    return sum



a,d,n = map(int,input().split())
print(sumofap(a,d,n))


OUTPUT

1 2 4 
16
