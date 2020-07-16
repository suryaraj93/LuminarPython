#SUM OF PRIME NUMBERS IN A RANGE

low=int(input("Enter low limit"))
up=int(input("Enter upper limit"))
sum=0
for i in range(low,(up+1)):
    flg=0
    for n in range(2,i):
        if(i%n==0):
            flg=1
            break
        else:
            pass
    if(flg==1):
       pass
    else:
        sum=(sum+i)
print("sum of prime is" , sum)

