cdate=29
cmonth=6
cyear=2020

bdate=int(input("Enter the birth date: "))
bmonth=int(input("Enter the birth month: "))
byear=int(input("Enter the birth year"))

years=(cyear-byear)
if(bmonth<cmonth):
    if(bdate<cdate):
        years=years-1
#months=(cmonth-bmonth)
#days=(cdate-bdate)
#8/6/2020 7/5/2019
print("Age=",years,"Years")