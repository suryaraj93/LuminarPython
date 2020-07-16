date=1
mon=7
yr=2020
bdate=int(input("enter day"))
bmon=int(input("enter month"))
byr=int(input("enter year"))
yrs=(yr-byr)
if(bmon>mon):
    yrs = yrs - 1
if (bmon > mon):
    if(bdate>date):
        yrs=yrs-1
print("age= ",yrs)