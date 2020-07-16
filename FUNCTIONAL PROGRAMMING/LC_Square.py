lst=[5,40,80,15]

#Normal method
squarelist=list(map(lambda x:x**2,lst))
print(squarelist)

#List comprehensive method
square=[(i**2)for i in lst]
print(square)

#PRINT PAIRS

lst=[1,2,3]
lst2=[4,5,6]

#Normal method
for i in lst:
    for j in lst2:
        print((i,j))
#List Comprehensive method
pairs=[(i,j) for i in lst for j in lst2]
print(pairs)

#i**j
power=[(i**j) for i in lst for j in lst2]
print(power)

#even
#even=[i for i in lst if i%2==0]
#print(even)

even=[i%2==0 for i in lst]
print(even)