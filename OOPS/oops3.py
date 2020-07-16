                                                                        #CONSTRUCTOR
class student:
    def __init__(self,name,rol,course):
        self.name=name
        self.rol=rol
        self.course=course
    def print(self):
        print(self.name,",",self.rol,",",self.course)
ob=student("ajay",100,"mca")
ob.print()
