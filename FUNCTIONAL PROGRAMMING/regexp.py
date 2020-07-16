import re
#x='[a-z][369][a-z]*'
# x='kl\d{2}[a-z]*\d{4}' #Vehicle number
# x='\d{10}' #phone number
x='[a-zA-Z]\w*@gmail[.]com'  #Email validation
vname=input("enter variable name")
match=re.fullmatch(x,vname)
if (match!=None):
    print("Valid")
else:
    print("Inavalid")