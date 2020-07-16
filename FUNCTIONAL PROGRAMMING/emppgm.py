#convert all employee name to upper case
#print salary greater than 15000
#provide increment of 5000 for all employee greater than equal to 2
#list all employees designation=developer


class Employee:
    def __init__(self,eid,name,desig,sal,exp):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.sal=sal
        self.exp=exp
    def printEmp(self):
        print(self.eid,",",self.name,",",self.desig,",",self.sal,",",self.exp)
f=open("C:/Users/user/PycharmProjects/LuminarPython/FUNCTIONAL PROGRAMMING/emplist")
emp=[]
for data in f:
    #print(data)
    employee=data.rstrip("\n").split(" ")
    #print(employee)
    eid=employee[0]
    name=employee[1]
    desig=employee[2]
    sal=int(employee[3])
    exp=int(employee[4])
    ob=Employee(eid,name,desig,sal,exp)
    ob.printEmp()
    emp.append(ob)
#PRINT UPPERCASE
print('\n')
uppercase=list(map(lambda Employee:Employee.name.upper(),emp))
print(uppercase)
print("\n")
#SALARY FILTER
salary=list(filter(lambda Employee:Employee.sal>15000,emp))
for value in salary:
    print(value.name)
print("\n")
#INCREMENT
increment=list(filter(lambda Employee:Employee.exp>=2,emp))
for val in increment:
    sal=val.sal+5000
    print(val.name,"'s updated salary is Rs",sal,"/-")
print("\n")
#DESIGNATION=DEVELOPER
desig=list(filter(lambda Employee:Employee.desig=="developer",emp))
for pos in desig:
    print(pos.name.upper())