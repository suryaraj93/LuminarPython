f=open("C:/Users/user/PycharmProjects/LuminarPython/FlowControls/test/data")
dict={}
for data in f:
    lst=data.rstrip("\n").split(",")
    print(lst)
    dis=lst[0]
    temp=lst[1]
    print(dis)
    print(temp)
    if (dis not in dict):
        dict[dis]=temp
    else:
        dict[dis]<temp
        dict[dis]=temp
print(dict)
