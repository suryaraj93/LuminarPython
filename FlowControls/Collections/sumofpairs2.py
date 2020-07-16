lst=[1,4,5,3,2]
lst.sort()
low=0
up=len(lst)-1
sum=int(input("Enter the sum "))
pairs=[]
while(low<up):
    res=(lst[low]+lst[up])
    if(res==sum):
        pairs.append((lst[low],lst[up]))
        low=low+1
    elif (res<sum):
        low=low+1
    elif(res>sum):
        up=up-1
print("Pairs are",pairs)
