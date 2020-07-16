lst=[10,9,7,8,5,6,3,2,4,1] #LIST
lst.sort() #SORT
low=0
upper=len(lst)-1
flag=0
element=int(input("Enter search element"))
while(low<upper):
    mid=(low+upper)//2
    if(element>=lst[mid]):
        low=mid+1
    elif(element==lst[mid]):
        flag=1
        break
    elif(element<lst[mid]):
        upper=mid-1
if (flag==1):
    print("Element found")
else:
    print("Element not found")



