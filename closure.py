# coluser is remeber varaibles or agruments from the outer scope even after the outer function is called and finsh exceuting 
# -------------------------------------------------------------------------------------------------
# nested function
def out():
    x=5
    def inn():
      print(x+5)
    inn()
out()
# -------------------------------------------------------------------------------------------
def outer(name):
    def inner():
       return name.upper()
    return inner()
name1 = outer("praveen")
print(name1)
# -------------------------------------------------------------------------------------------------
def outside(x,y):
    def inside():
        return x+y
    return inside()
sum1 = outside(10,10)
print(sum1)
# ----------------------------------------------------------------------------------------------
from functools import partial
# partial is used reduce or fix some agruments in a fuction and it create a new function 
def taxrates(income,tax):
    return income * (1+tax)
set_taxrates = partial(taxrates,tax=0.18)
print(set_taxrates(1000))
print(set_taxrates(2000))
# -------------------------------------------------------------------------------------
# composed function is ouput from an function is goes to the input to the another function like f(g(x))
def add(x):
    return x+2
def multiply(x):
    return x*2
def composed(x): # multiply ==> 2*2 == 4, ADD ==> 4+2 == 6 
    return add(multiply(x))
print(composed(2))
# --------------------------------------------------------------------------
# clousre 

def parent():
  message = "hello"
  def chlid():
      message = "world"
  print(message)
  return chlid()
  message = "praveen"
 
parent() 

def number_outer():
    number=[]
    def number_inner(x):
        number.append(x)
        print(number)
    return number_inner

num = number_outer()
num(3)
num(4)
num(5)
# --------------------------------------------------------
# callback
def func(call):
    print(f"first call back function")
    call()
    
def greet():
    print(f"this is second function")
def greet1():
    print(f"this is third function")
func(greet1)


def sum(back,x,y):
    result = x+y
    back(result)
def display_result(result):
    print(result)
    
sum(display_result,3,3)
# ----------------------------
# sum(display_result, 3, 3)
#         ↓
# result = 3 + 3
#         ↓
# back(result)
#         ↓
# display_result(6)
#         ↓
# print(6)