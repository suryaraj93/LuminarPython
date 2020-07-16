#PRIME OR NOT USING FUNCTION.

def check(num):
    flg=0
    for i in range(2,num):
        if (num%i==0):
            flg=1
            break
        else:
            pass
    if(flg>0):
        print("not prime")
    else:
        print("prime")
check(9)
