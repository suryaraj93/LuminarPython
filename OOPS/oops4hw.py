class student:
    def __init__(self,rol,name,course,marks):
        self.rol=rol
        self.name=name
        self.course=course
        self.marks=marks
    def print(self):
        print(self.rol,self.name,self.course,self.marks)
f=open("C:/Users/user/PycharmProjects/LuminarPython/OOPS/studentlist")
std=[]
for data in f:
    print(data)
    students=data.rstrip("\n").spilt(" ")
    print(data)