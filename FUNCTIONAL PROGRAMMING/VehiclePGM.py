
f=open("C:/Users/user/PycharmProjects/LuminarPython/FUNCTIONAL PROGRAMMING/numberlist")
import re
x='KL\d*[a-z]*\d*'
# f=open("C:/Users/user/PycharmProjects/LuminarPython/FUNCTIONAL PROGRAMMING/numberlist")
fw=open("updated.txt","w")
for data in f:
    num=str(data)
    print(num)
# vnum=re.fullmatch(x,num)
# if (vnum!=None):
#     print("valid",data)