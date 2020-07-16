#CLASS
#OBJECT
#REFFERENCE
                                                                   #EMPLOYEE
class employee:
    def setValues(self,id,name,desig,comp):
        self.id=id
        self.name=name
        self.desig=desig
        self.comp=comp
    def printValues(self):
        print("ID :",self.id)
        print("NAME :",self.name)
        print("DESIG :",self.desig)
        print("COMP :",self.comp)
ob1=employee()
ob1.setValues(100,"VIJAY","Manager","ABC")
ob1.printValues()
ob2=employee()
ob2.setValues(101,"AJAY","EMPLOYEE","ABC")
ob2.printValues()