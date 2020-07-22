import functools
class employee:
    def __init__(self,id,name,desig,mail,sal):
        self.id=id
        self.name=name
        self.desig=desig
        self.mail=mail
        self.sal=sal
    def printvalues(self):
        print(self.id,self.name,self.desig,self.mail,self.sal)

f=open("empdata")
emp=[]
for data in f:
    #print(data)
    details=data.rstrip("\n").split(",")
    # print(details)
    id=details[0]
    name=details[1]
    desig=details[2]
    mail=details[3]
    sal=int(details[4])
    ob=employee(id,name,desig,mail,sal)
    emp.append(ob)
    # print(emp)
    ob.printvalues()

salary=functools.reduce(lambda o1,o2: o1 if o1>o2 else o2,list(map(lambda o1:o1.sal,emp)))
print(salary)