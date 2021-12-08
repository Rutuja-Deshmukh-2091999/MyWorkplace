def cal(celsius):
    fahrenheite = (celsius * 1.8)+32
    return fahrenheite

celsius = float(input("Enter the Temperature in Celsius"))
fahrenheite = cal(celsius)
print("The %.2f degree Celsius is equal to: %.2f Fahrenheit"%(celsius,fahrenheite))

