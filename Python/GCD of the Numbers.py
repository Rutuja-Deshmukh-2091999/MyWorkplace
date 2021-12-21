def gcdofno(x,y):
    if x > y:
        temp = y
    else:
        temp = x
    for i in range(1,temp + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd

x = int(input("Enter the First Number"))
y = int(input("Enter the Second Number"))
result = gcdofno(x,y)
print(result)

import os.path

save_path = r"C:\Users\User\PycharmProjects\pythonProject1"

name_of_file = input("What is the name of the file: ")

completeName = os.path.join(save_path, name_of_file+".txt")

file1 = open(completeName, "w+")

file1.write(str(result))


file1.close()
