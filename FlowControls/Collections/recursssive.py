string = input("Enter text ")
words=list(string)
dict={}
flg=0
for i in words:
    if (i not in dict):
        dict[i]=1
    else:
        dict[i]+=1
        flg=1
        print("the letters are ",i)
        break
if(flg==0):
    print("no recurring")

