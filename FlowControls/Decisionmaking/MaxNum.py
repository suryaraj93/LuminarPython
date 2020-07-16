num1=int(input( "number 1: "))
num2=int(input("number 2: "))
num3=int(input("number 3:"))

if(num1>num2)&(num1>num3):
    print("Max = ",num1)
if(num2>num1)&(num2>num3):
    print("max=",num2)
if(num3>num1)&(num3>num2):
    print("max=",num3)