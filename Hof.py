def email_gmail(username,mail="email.com"):
    print(f"{username}@{mail}") 
def hot_gmail(username,mail="hotmail.com"):
    print(f"{username}@{mail}")
def ymail_gmail(username,mail="ymail.com"):
    print(f"{username}@{mail}")   
def full_mail(username,mail_fun ):
    return mail_fun(username)
full_mail("praveen",email_gmail)
full_mail("kishore",hot_gmail)
full_mail("karthi",ymail_gmail)
# ---------------------------------------------------------
def fun1(name):
    return f"Hello {name}"
def fun2(invite):
    return invite("praveen")
def fun3(invite2):
    return invite2("kumar")
print(fun2(fun1))
print(fun3(fun1))
# ------------------------------------------------
def outer(msg):
    def inner():
        return msg.upper()
    return inner
fun=outer("surya")
# print(type(fun))
print(fun())
# -------------------------------
add = lambda a,b : a+b 
print(add(2,2))
# --------------------------------------
square = lambda x : x ** x
print(square(2))
# -----------------------------
def sqr(x):
    return x**x
number = [1,2,3,4,5,6]
squared = map(sqr,number)
print(list(squared))
mapping = ["apple","Orange","MAngo","grapes","cherry"]
def to_be_mapped(x):
    return x.upper()
mapped = map(to_be_mapped,mapping)
print(list(mapped))
mapp = list(map(lambda x:x.lower(),mapping))
print(mapp)
num = list(map(lambda no : no*2,number))
print(num)
tup = (1,2,3,4,5,6)
even = list(map(lambda evens:evens %2==0,tup))
print(even)

dic = {
    "name":"praveen",
    "age":21,
    "gender":"male",
    "dept":"IT"
}

m = list(map(lambda n:str(n).upper(),dic.items()))

print(m)

eve = tuple(filter(lambda x: x%2==0,tup))
print(eve)


word = ["PRAVEEN","SURYA","premkesh","tharun"]

words = list(filter(lambda z : z == z.upper(),word))
print(words)
# --------------------------------------
from functools import reduce
red = reduce(lambda x,y:x*y,number)
print(red)
reds = reduce(lambda a,b : a + " KUMAR " + b.upper() ,word)
print(reds)