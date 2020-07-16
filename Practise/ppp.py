l=int(input("enter lower"))
u=int(input("enter upper "))

for i in range(2,(u+1)):
    flg=0
    for j in range(2,i):
        if(i%j==0):
            flg=1
    if flg>0:
        pass
    else:
        print(i,"P")