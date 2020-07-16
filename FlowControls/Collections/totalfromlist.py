#PRINT PAIRS OF SUM OF FROM LIST

list=[1,2,3,4]
total=int(input("Enter the sum = "))
for i in list:
    for j in list:
        if(i+j==total):
            print("pairs = ",i,j)


