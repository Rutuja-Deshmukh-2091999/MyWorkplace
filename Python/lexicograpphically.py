from itertools import combinations

a = input()
b = combinations(a,2)
list1 = list(b)
ls = min(list1)
str1 = ''
for i in ls:
    str1 += i
print(str1)
