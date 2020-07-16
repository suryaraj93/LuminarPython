name=input("Enter name: ")
a=int(input("mark 1: "))
b=int(input("mark 2: "))
c=int(input("mark 3: "))
total=a+b+c
print("total",total)
if(total>145):
    print("A+")
elif(total>140)&(total<=145):
    print("A")
elif(total>135)&(total<=140):
    print("B+")
elif(total>130)&(total<=135):
    print("B")
elif(total<=130):
    print("Failed")
else:
    print("INVALID")