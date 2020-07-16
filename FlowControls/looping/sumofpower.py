num=int(input("Enter number"))
res=0
while(num>0):
    digit=(num%10)
    res=(digit**3)+res
    num=num//10
print(res)
