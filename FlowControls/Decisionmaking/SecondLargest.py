num1=int(input("Number 1: "))
num2=int(input("Number 2: "))
num3=int(input("Number 3: "))

if(num1>num2)&(num1>num3):
    if(num3>num2):
        print("Second largest",num3)
else:
    print("Second largest",num2)
if(num2>num1)&(num2>num3):
   if(num3>num1):
       print("Second largest",num3)
else:
    print("Second largest",num1)
if(num3>num2)&(num3>num1):
    if(num1>num2):
        print("Second largest",num1)
else:
   print("Second largest",num2)