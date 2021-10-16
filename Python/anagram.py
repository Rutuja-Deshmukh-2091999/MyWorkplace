from itertools import permutations
a = input()
b = input()
c = permutations(a)
d = permutations(b)
li2 = []
for i in d:
    if i in c:
        li2.append("Yes")
    else:
        li2.append("No")
if 'Yes' in li2:
    print('Yes')
else:
    print('No')