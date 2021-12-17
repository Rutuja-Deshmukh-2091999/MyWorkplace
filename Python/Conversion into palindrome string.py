str1 = input("Enter the String - ")
temp = str1
str1 = str1[::-1]
str2 = temp + str1[1:]
print(str2 , "is a palindrome")

