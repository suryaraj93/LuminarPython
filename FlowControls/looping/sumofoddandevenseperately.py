limit=int(input("enter the range"))
i=0
oddsum=0
evensum=0
while(i<=limit):
    if(i%2==0):
        evensum=evensum+i
        i+=1
    else:
        oddsum=oddsum+i
        i+=1
print("sum of even is",evensum)
print("sum of odd is ",oddsum)

