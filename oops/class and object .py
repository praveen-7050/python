# class userInfo():
#     name="praveen"
#     Age = 22
# user = userInfo()
# print(f"the user name is {user.name} and the {user.name} age is  {user.Age}")

# class F1:
#     def __init__(self,teamname,drivername,champoianship):
#         self.teamname = teamname 
#         self.drivername = drivername
#         self.champoianship = champoianship
#     def display(self):
#         print(f"The Team name is {self.teamname} and the dirver are {self.drivername} and they own the both {self.champoianship} championship")

# forumla = F1("Maclren","Lando and Oscar","Drivers and constructor")
# forumla.display()


# class person(): # class creation
#     def __init__(self,name,age): # state / data
#         self.name = name
#         self.age = age

#     def persons(self) : # behaviour 
#         print(f"the person Name is {self.name} and the age is {self.age}")


# user = person("praveen",21) # object creation
# user.persons()
# user1 = person("ravi",22)
# user1.persons()
# class car:
#     def __init__(self,name,price,features,model,color,engine):
#         self.car_Name = name 
#         self.car_price=price
#         self.car_features = features
#         self.car_model= model
#         self.car_color = color
#         self.car_engine = engine
#     def display(self):
#         print(f"""The car Name is {self.car_Name} and the price of the car is {self.car_price} 
# and the features of the car is  {self.car_features} and the model of the car is {self.car_model}
# and the color os the car is {self.car_color} and the engine {self.car_engine} """)

# about_car = car("Mercedes",10000,"AC",2021,"White","v3")
# about_car.display()

# class userinfo(): # class
#     def __init__(self,number,Addhar_No): # state or method 
#         self.number = number 
#         self.An=Addhar_No
    
#     def dis(self): # behaviour / action #static method  without constructor 
#         print(f"the Mobile Number is {self.number} and the Adhhar Number is{self.An}")
#     def  add (a,b):
#         return a+b 
# details = userinfo(1234567,22446688)
# details.dis()
# print(userinfo.add(2,2))

# class praveen:
#     def __init__(self,gender,age):
#         self.gender = gender
#         self.age = age
# nameof = praveen("male",22)
# del nameof.age
# print(nameof.gender)
# print(nameof.age)

# class Person:
#   def __init__(self, name, age=22):
#     self.name = name
#     self.age = age

# p1 = Person("Tobias")
# print(p1.age)

# p1.age = 27
# print(p1.age)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def celebrate_birthday(self):
#     self.age += 1 # behaviour change every calling 
#     print(f"Happy birthday! You are now {self.age}")

# p1 = Person("Linus", 25)
# p1.celebrate_birthday()



# class Playlist:
#   def __init__(self, name):
#     self.name = name
#     self.songs = [] #  instance 

#   def add_song(self, song):
#     self.songs.append(song)
#     print(f"Added: {song}")

# my_playlist = Playlist("Favorites")
# my_playlist.add_song("Bohemian Rhapsody")``
# my_playlist.add_song("Stairway to Heaven")

# class Person:
#   species = "" # Class property

#   def __init__(self, name):
#     self.name = name # Instance property

# p1 = Person("Emil json")
# p1.type = "four legs"
# p1.species = "Animal"
# p2 = Person("Tobias")

# print(p1.name)
# print(p2.name)
# print(p1.type)
# print(p1.species)
# print(p2.species)

class car:
    wheels  = 4 

    def __init__(self,brand):
        self.brand = brand 

car1 = car("honda")
car2 = car("Ferrari")

print(f" The car name is {car1.brand} and the car has {car1.wheels} wheels")
print(f" The car name is {car2.brand} and the car has {car2.wheels} wheels")
# print(car2.wheels)
# print(car1)
# print(car2)