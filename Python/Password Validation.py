def passvalid(str1):
    list1 = ['!','#','@','$','%','^']
    vali = True

    if len(str1) < 6:
        print("Password should be at least 6")
        vali = False

    if len(str1) > 15:
        print("Length should not be greater than 15")
        vali = False

    if not any(char.isupper() for char in str1):
        print("Password should have atleast one uppercase character")
        vali = False

    if not any(char.islower() for char in str1):
        print("Password should have atleast one lowercase character")
        vali = False

    if not any(char in list1 for char in str1):
        print("Password should have atleast one special character")
        vali = False

    if vali:
        return vali

password = input("Enter the Password - ")

if (passvalid(password)):
    print("Password is Valid")
else:
    print("Password is Invalid")

