num = int(input())
rev = 0
temp = num
while num != 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if(temp == rev):
    print("Number is palindrome")
else:
    print("Its not a palindrome")