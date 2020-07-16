f=open("C:/Users/user/Downloads/redataset/complete.csv","r")
i=0
dict={}
for lines in f:
    report=lines.rstrip("\n").split(",")
    state=report[1]
    cases=int(report[4])
    if(state not in dict):  #statewise
        dict[state]=cases
    else:
        dict[state]=cases
print(dict)
total=[]
for k,v in dict.items():    #totalcase
    total.append(v)
print("total cases =",sum(total))
sortlist=[]
for k,v in dict.items():
    sortlist.append((v,k))
    sorteddata=sorted(sortlist,reverse=True)
print(sorteddata[0:3])



