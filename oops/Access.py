# there are three methods in the access specifiers
# public - access everywhere normla class 
# _procteded
# __private 

class student:
    def __init__(self,name,age):
        self.name = name  # publicly delcaring 
        self.age = age
        
    def nameofstu(self):
        print(f"The name of the student is {self.name} and the age of the {self.name} is {self.age}") 
    
stu = student("praveen",22) # accssing globally and publicy so this public access specifier.
stu.nameofstu()
# ----------------------------------

class staff:
    def __init__(self,staffname,staffage):
        self._staffname = staffname
        self._staffage = staffage
    def staffDetails(self):
     try:
        print(f"The Name of the {self._staffname} and the age of the staff is {self._staffage} ")
     except Exception as e:
         print(f"The is procted method so use the annotations as {e}")
         
class Hm(staff):
    def staffDetails(self):
     try:
        print(f"The Name of the {self._staffname} and the age of the staff is {self._staffage} to the pricipal ") #accessing through the proctoed method s
     except Exception as e:
         print(f"The is procted method so use the annotations as {e}")
         
        
cstaff = staff("mukesh",22)
cstaff.staffDetails()
madam = Hm("kumar",50)
madam.staffDetails()
print("successfully handle the error ")

class company:
    def __init__(self,name,Department,salary):
        self.name = name
        self._Department = Department
        self.__salary = salary 
    
    def empSalary(self):
        print(f"The salary of the employeee is {self.__salary} and the name of the employee is {self.name} and the department of the employee is {self._Department}")
        
comp = company(20000,"praveen","IT")
comp.empSalary()