import re
f=open("empdata")
fw=open("validmails","w")
mid=[]
for data in f:
    details = data.rstrip("\n").split(",")
    mail=details[3]
    mid.append(mail)
print(mid)

for i in mid:
    x='[a-zA-Z]\w*@gmail[.]com'
    match=re.fullmatch(x,i)

    if (match!=None):
        fw.write(i+"\n")
    else:
        print("unvalid mail ids are: ",i)