withdrawl,balance  = list(map(float,input().split()))
if withdrawl %5==0 and (withdrawl + 0.50) <= balance:
    print(round(balance-(withdrawl+0.50 ),2))
else:
    print(round(balance,2))
