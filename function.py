
"""
def greet():
    print("Hello World")

greet()
"""


def person_Details(name,age=18):
    print(f"His name is {name} and his age is {age}")

person_Details("praveen",21)
person_Details("surya",22)
person_Details("Tharun",22)
person_Details("prem")

print(type(person_Details))


def factorial(n):
    result =1
    for i in range(1,n+1):
        result *=i
    return result 

print(factorial(5)) 

def add(a,b) :
    return a+b


# result = add(10,10)


def userdetails(**user_details): #keyword arguments
    for key,value in user_details.items() :
        print(f"{key}:{value}")
userdetails(name="praveen",age=21,Gender="male",isAlive="True")