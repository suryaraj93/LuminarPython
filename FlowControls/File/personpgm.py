f=open("C:/Users/user/PycharmProjects/LuminarPython/FlowControls/File/person")
emp={}
for data in f:
    value=data.rstrip("\n").split(",")
    print(value)
    id=value[0]
    name=value[1]
    age=value[2]
    desig=value[3]
    exp=value[4]
    sal=value[5]
    if id not in emp:
        emp[id]={'id':id,"name":name,"age":age,"desig":desig,"exp":exp,"sal":sal}
    else:
        pass
for k,v in emp.items():
    print(k,"\t",v)

def printemployee(**kwargs):
    #for k,v in kwargs.items():
       # id=v
        #if(id in emp):
       #     print(emp[id]["name"])
       # else:
           # print("theres no employee",id)
    #props=kwargs['property']
    #id=kwargs["id"]
   # print(emp[id]["name"])
    #print(emp[id][prop])
    #print(id,"\t",prop)
#printemployee(id="101")
    if "id" in kwargs:
        id=kwargs["id"]
        if id in emp:
            print("employee name",emp[id]["name"])
        else:
            print("no employee")
    if "property" in kwargs:
        prop=kwargs["property"]
        print(emp[id][prop])
printemployee(id="101",property="desig")

