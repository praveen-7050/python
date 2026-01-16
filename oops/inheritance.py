# class Dad: #parent class
#     def house(self):
#         print(" I am from the parent class  ")

# class Son(Dad): # child class
#     def house1(self):
#         print(" I am  from the child class")

# dad1 = Dad()
# dad1.house()
# son1 = Son()
# son1.house()
# son1.house1()
# --------------------------------------------------------------------------------------------------------

# class Parent:
#    def first(self,pname):
#       self.Parentname =pname
#       print(f"The Name of the parent is {self.Parentname}")

# class Child(Parent):
#    def second(self,cname):
#       self.childname = cname
#       print(f"the child Name is {self.childname}")

# class Child2(Child):
#    def third(self,cname1):
#       self.cname1= cname1
#       print(f"the 2 child name is {self.cname1}")

#    def first(self,name):
#         self.name = name
#         print(f"The second parent {self.name} ")
# obj1 = Child2()
# obj1.first("praveen")
# obj1.second("tharun")
# obj1.third("mani")
# obj1.first("praveen kumar")

# ------------------------------------------------------
# multiple class in single class
# class a:
#     def one(self,z):
#         self.a =z 
#         print(f"The a is {self.a}")
# class b:
#     def two(self,y):
#         self.b = y
#         print(f"The b is {self.b}")

# class c(a,b):
#     def three(self,x):
#         self.c = x 
#         print(f"The c is {self.c} ")

# obj2 = c()
# obj2.one(1)
# obj2.two(2)
# obj2.three(3)
# ----------------------------------------------------------------------------------------
#one page to another page 
# class Grandparent:
#     def Gp(self):
#         print("This is Grand parent")
# ------------------------------------------------------------------------------

# class Vechile:
#     def __init__(self,vname,vtype,vprice):
#         self.vname= vname
#         self.vtype = vtype
#         self.vprice=vprice
#     def vech(self):
#         print(f"the {self.vname} and the type of the vechile is {self.vtype} and the price of the {self.vname} is around {self.vprice}")
# class Car(Vechile):
#     def __init__(self,cname,ctype,cprice):
#         super().__init__(cname,ctype,cprice)

#     def aboutcar(self):
#         print(f"the {self.vname} and the type of the vechile is {self.vtype} and the price of the {self.vname} is around {self.vprice}")

# automobile = Car("audi",2022,1200000)
# automobile.aboutcar()
# # automobile.vech()

# autovechile = Vechile("car","Four-wheeler",100000)
# autovechile.vech()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# class A:
#     def show(self):
#         print("A")

# class B(A): # calls a and overdie the a A into B
#     def show(self):
#         print("B")

# class C(A): # calls A but overide into B so here a is B  and c ovride the a B into C c is c
#     def show(self):
#         print("C")

# class D(B, C):  # calls b,c output is b so it is b
#     pass

# obj = D()
# obj.show()  # Output: B (follows MRO)
# print(D.mro())  # Shows method resolution order
# --------------------------------------------------------------------------------------------------------------