lst=[1,2,3,4,5]
even=[]
od=[]
for num in lst:
    if(num%2==0):
        even.append(num**2)
    else:
        od.append(num**2)
print("evenlist",even)
print("oddlist",od)
