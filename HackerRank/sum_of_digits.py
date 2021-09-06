n = int(input())

def sumd(n):
    sum = 0
    for i in str(n):
        sum = sum + int(i)
    
    return sum
print(sumd(n))
        
