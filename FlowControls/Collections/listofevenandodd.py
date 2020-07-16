#LIST OF EVEN AND ODD

lst=[1,2,3,4,5]
even=[]
od=[]
for num in lst:
    if(num%2==0):
        even.append(num)
    else:
        od.append(num)
print("evenlist",even)
print("oddlist",od)
