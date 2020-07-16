#ELEMENTS SEARCHING

lst=[10,11,12,13,14,15,16,17]
element=int(input("Enter element for searching"))
flag=0
for i in lst:
    if (i==element):
        flag=1
        break
    else:
        pass
if(flag==1):
        print("element in list")
else:
        print("element not in list")