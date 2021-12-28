from itertools import permutations
str1 = input()
count = 0
a = permutations(str1)
for i in a:
    i = "".join(i)
    if (i[::-1] == i):
        count += 1
if count >= 1:
    print("string can be converted into plaindrome")
else:
    print("string cannot be converted into plaindrome")



