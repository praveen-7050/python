# class myclass:
#     def instance_method(self,name):
#         print(f"this is instance method {name}")
#     @classmethod
#     def class_method(cls,age):
#         print(f"this is class method {age}")
#     @staticmethod
#     def static_method(dept):
#         print(f"this is static method {dept}")
        
# obj= myclass()
# obj.instance_method("praveen")
# myclass.class_method(22)
# myclass.static_method("IT")

# -----------------------------------------------------

# class method

class student :
    college_name = "KPRCAS"
    
    def __init__(self,name,dept):
        self.name =name
        self.dept =dept
    @classmethod
    def display_details(cls,clg_name):
        cls.college_name = clg_name
    def display_method(self):
        print(f"The name of the student is {self.name} and the department of the student is {self.dept} and the name of the college is {self.college_name}")
    @staticmethod
    def staff_details(name):
        return(f'the name of the staff is {name}')
        
stu1 = student("praveen","IT")
stu1.display_details("PSGCAS")
stu1.display_method()
print(student.staff_details("mukesh"))