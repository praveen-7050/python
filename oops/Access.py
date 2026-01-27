# there are three methods in the access specifiers
# public - access everywhere normla class 
# _procteded
# __private 

# class student:
#     def __init__(self,name,age):
#         self.name = name  # publicly delcaring 
#         self.age = age
        
#     def nameofstu(self):
#         print(f"The name of the student is {self.name} and the age of the {self.name} is {self.age}") 
    
# stu = student("praveen",22) # accssing globally and publicy so this public access specifier.
# stu.nameofstu()
# ----------------------------------

# class staff:
#     def __init__(self,staffname,staffage):
#         self.__staffname = staffname
#         self.__staffage = staffage
#     def staffDetails(self):
#      try:
#         print(f"The Name of the {self.__staffname} and the age of the staff is {self.__staffage} ")
#      except Exception as e:
#          print(f"The is procted method so use the annotations as {e}")
         
# class Hm(staff):
#     def staffDetails(self):
#      try:
#         print(f"The Name of the {self._staff__staffname} and the age of the staff is {self._staff__staffage} to the pricipal ") #accessing through the proctoed method s
#      except Exception as e:
#          print(f"The is procted method so use the annotations as {e}")

# class princpal(Hm):
#     def staffDetails(self):
#      try:
#         print(f"The Name of the {self._staff__staffname} and the age of the staff is {self._staff__staffage} to the pricipal ") #accessing through the proctoed method s
#      except Exception as e:
#          print(f"The is procted method so use the annotations as {e}")
           
         
        
# cstaff = staff("mukesh",22)
# cstaff.staffDetails()
# madam = Hm("kumar",50)
# madam.staffDetails()
# print("successfully handle the error ")
# prince = princpal("Kumathadevi",56)
# prince.staffDetails()
# -----------------------------------------------------------------
# class company:
#     def __init__(self,name,Department,salary):
#         self.name = name
#         self._Department = Department
#         self.__salary = salary
#     def empSalary(self):
#         print(f"The salary of the employeee is {self.__salary} and the name of the employee is {self.name} and the department of the employee is {self._Department}")
        
# comp = company(20000,"praveen","IT")
# comp.empSalary()
# -------------------------------------------------------------------------------


class college:
    def __init__(self,name,id_no,dept):
        self.name =  name
        self.__id_no = id_no # private
        self._dept = dept #procted
        
    # def get_id(self):
    #     return self.__id_no
    # def get_dept(self):   # these are useless
    def get_details(self):
        return self.__id_no,self._dept        
    def details(self):
        id,dept=self.get_details()
        return f"The name the of the student is {self.name} and the id of the student is {id} and the dept of the student is {dept}" 
    
col = college("praveen",2288,"B.COM CA")
print(col.details())

class stu_college(college):
    def details(self):
     id_no,dept = self.get_details()
     print(f"The name the of the student is {self.name} and the id of the student is {id_no} and the dept of the student is {dept}")
    
stu1 = stu_college("suresh",2289,"B.SC(CS)")

stu1.details()