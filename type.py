a = 10
print(a,type(a))
b = 10.00
print(b,type(b))
c = "20"
print (int(c),type(c))
# print(b+c) # oprend error
x=int(c)
print(x,type(x))

y="10"
z ="10"
print(int(y)+int(z))
print(type(y))


val =True
print(type(int(val)))

val1 =10
val2 =2
# ---------------Arthmeic---------------------------
print(val1+val2) # add
print(val1-val2) #sub
print(val1*val2) # multiple
print(val1/val2) # div quation
print(val1%val2) # modules reminder
print(val1//val2) # div not give in point
print(val1**val2)  # exponstinal 10* 10* 10

#-------------------comparsion---------------------------------

comp1 = 10
comp2 = 20

print(comp1==comp2)
print(comp1>=comp2)
print(comp1<=comp2)
print(comp1!=comp2)
print(comp1>comp2)
print(comp1<comp2)

#--------------logical---------------------

p = True
n = False

print(p and n)
print(p or n)
print (not p)
print(not n)

s='hello'
t=s
s=s.upper()
print(t)

x='hello world'
print('world'in x) 
