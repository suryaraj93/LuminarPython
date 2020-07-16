lst=[10,20,30]
num1=int(input("Enter num 1"))
num2=int(input("enter num 2"))
index=int(input("enter index"))
try:
    res=num1/num2
    print("result is ", res)
    print(lst[index])

except Exception as f:
    print(f.args)

finally:
    print("ok bye")