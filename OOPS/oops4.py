                                                                            #EMPLOYEE
class employee:
    def __init__(self,eid,name,sal,exp):
        self.eid=eid
        self.name=name
        self.sal=sal
        self.exp=exp
    def printEmp(self):
        print(self.eid,",",self.name,",",self.sal,",",self.exp)
f=open("C:/Users/user/PycharmProjects/LuminarPython/OOPS/employeelist")
empLst=[]
for data in f:
    #print(data)
    employees=data.rstrip("\n").split(",")
    eid=employees[0]
    name=employees[1]
    sal=int(employees[2])
    exp=employees[3]
    ob=employee(eid,name,sal,exp)
    empLst.append(ob)
    ob.printEmp()
for employee in empLst:
    if (employee.sal>17000):
        print(employee.name.upper())  #upperfunction for capitalizing

