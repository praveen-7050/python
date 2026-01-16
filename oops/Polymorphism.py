# class father:
#     def house(self):
#         print("house white")

# class daughter(father): #inherits the fathers :
#     def factory(self):
#         print("factory")
#     def house(self):
#         print("house red")


# family = daughter()
# family.factory()
# family.house()


# class payment:
#     def process(self):
#         pass 
# class Creditcard(payment):
#     def process(self):
#         print("Processing through credit card")
# class Upi(payment):
#     def process(self):
#         print("Processing through upi")
# class Paypal(payment):
#     def process(self):
#         print("Processing through paypal")
# pay = [Creditcard(),Upi(),Paypal()]
# for payments in pay:
#     print(payments.process())

class Animal:
    def sound(self):
        return "some sound"
class Dog:
    def sound(self):
        return "bark"

class Cat:
    def sound(self):
        return "meow"
dog = Dog()
cat = Cat()
print(dog.sound())
print(cat.sound())