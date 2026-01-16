from inheritance import Grandparent
class Parent(Grandparent):
     def par(self):
          print("This is parent")
    
obj3 = Parent()
obj3.Gp()
obj3.par()