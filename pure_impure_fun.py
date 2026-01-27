# impure function
total= 0

def sumof(amount):
    global total  
    total += amount
    print(f"The value of the sumof function is {total}")
    
sumof(4)
sumof(4)

print(total)
# -------------------------------------------
# pure function
def add(a,b):
    return a+b
adding = add(10,10)
print(adding)

def sub(a,b):
   if a < b:
       return " the value a should be greate than b"
   else :
        return a-b
    
subract = sub(30,20)
print(subract)
