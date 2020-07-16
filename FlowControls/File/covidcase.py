f=open("C:/Users/user/PycharmProjects/LuminarPython/FlowControls/File/complete")
case={}
for data in f:
    case=data.rstrip("\n").split("\t")
    print(case)
    state=case[1]
    totcon=case[4]
    cured=case[6]
