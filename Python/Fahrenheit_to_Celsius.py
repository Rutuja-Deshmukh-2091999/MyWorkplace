def cal(Fahrenheite):
    Celsius = (Fahrenheite + 32)/1.8
    return Celsius

Fahrenheit = float(input("Enter the Temperature in Fahrenheit"))
Celsius = cal(Fahrenheit)
print("The %.2f degree Fahrenheit is equal to: %.2f Celsius"%(Fahrenheit,Celsius))