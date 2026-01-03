#  interpreted high level genral purpose programming language,it supports both object oriented and function based programming
# software: an automated solution for real world problem
# program : a set of instruction which is given hardware to perform some specfic task,using which we can create software
#
# guido van rossum -> netharland -> 1991 feb 20 -> big fan of "monty python flying circus" tv series -> "Python"
# 
# open source
# platform indepedent
# platform --> os+processor  [windows,mac,linux]
# 
# compiler vs interpretter

# print("hello")


# source code --->compiler --> byte code --> pvm(python virtual machine) -> o/p


# variable:
#a container used to store the data
#rules:
#single char/descriptive word
# a=23
# age=23 
#does not starts with numbers
# a1=10
#alpha/numeric/special char(_)



# a="surya"
# print(type(a))


# #why python:
# #strongly typed languagev[we can not perform op between two diff data types]
# # a=10 #data type:int
# # # print(type(a))
# # b='ten' #string
# # print(a+b)

# #dynamic typing
# # a=10

# # a="gcp"

# #dynamic inference:

# #int a=10  #other programming language
# # a=10.234
# # print(type(a))


# #automatic memory management:
# # a=10
# # print(id(a))

# # b=12
# # print(id(b))



# #data types:
# #int #whole number =10,20,30
# #float #10.2,10.5,10.25
# #string  #collection of char whcih is enclosed by single or double quote ['sql',"python"]
# #boolean #true/false


# # print("hello")

# #source code ---> interpreter[ compiler --> bytecode --> pvm(python virtual machine)]-->output

# # a=21
# # print(id(a))

# # a=10
# # b=20
# # print(a+b)


# #variable:
# #it is a container using which we can store the data

# a=10 #a --> variable

# #rules for variable dec:
# #variable name can either single char/descriptive word

# a=22
# age=22

# #variable can have number but it does not starts with number
# a1=10
# # 1a=10

# #variable name can have letters,numbers,spl char(_)

# first_name="sql"
# a= 'interpreter','compiler'
# # print(type(a))
# # for i in a:
# #     print(i)

#comments:
#single line comments
#multi line comments


#single line comments
# print("one")

#multi line comment

'''
print("one")
print("one")
print("one")
print("one")
print("one")
print("one")
'''

# a,b,c=10,20,30
# print(a,b,c)


# a=b=c=30
# print(a,b,c)


#inputs
#static input 
#dynamic input


#static input
# a=10
# print(a)
# print(a)
# print(a)
# print(a)

#dynamic input/user  input

# a=input()
# print(type(a))
# print("user input is:",a)

# type casting:
#conversion of one data type into another data type

# a=int(input("enter the no:"))
# print(type(a))
# print("user input is:",a)


# foramting
# a=10
# print(f"value of a is: {a}")
# print("value of a is:",a)


#operators:
#arithmetic operator
#assignment oprator
#raltional/comparison operator
#logical opeartor
#bitwise operator
#membership and identify operator

#arithmetic operator:
# print(1+1) #2
# print(1-1)  #0
# print(2*2)  #4
# print(2/2) #div float 1.0
# print(2%2)  #remainder #0
# print(2//2)  # floor div #int #1
# print(2**2) # expo #4


#assignment operator

# a=10
# a+=1  # a=a+1 #11
# a-=1  #a=a-1 #10
# a*=2 #a=a*2 #20
# # a/=2 #a=a/2 #10.0
# a//2  #a=a//2 #10 

# a%=2 #a=a%2 #0

# a**=2 #a=a*a
# print(a)


#comparison/relational operator
#it always returns boolean values

#>,<,>=,<=,==,!=

#greater than
# print(10>9)  # ten is greater than nine #true
# print(10>10)
# print(10>=10) #greater than or equal to 

# print(10<20) #less than 
# print(10<=10)  #less than or equal to  

# print(10 == '10')

# print(10 != 10)  #not equal to


#logical operator

#and,or,not

#and
# a=0
# print(a>0 and a<10)  #true and true

#or
# print(a>0 or a<10)  #false or true

#not
#true  --> false
#false --> true

# print(not(a<10)) #not(false) #true

#membership and identify operator:

#identify operator

# a=10
# print(id(a))
# b=10
# print(id(b))

# a=[1,2,3,4]
# print(id(a))
# b=[1,2,3,4]
# print(id(b))
#is,is not
# print(a is b)
# print(a is not b)


#membership operator:

#in,not in

# print('z' in "python")
# print('z' not in 'python')

#bitwise operator:
#&,|,~,^,>>,<<

# and,or,not,xor,right shift,left shift

# xor
# print(1^2)    

#0001
#0010
#0011

#right shift >>
# print(2>>2)

#0010>>1
#0001

#left shift
#print(2<<1)

#0010 << 1
#0100 #4


#control statements:
#used to control the flow of the program

# 1.conditional statement #if,if else,elif
#2.iterators(loops)

#conditional statement:
# a=5
# if(a>0):
#     print("statement is true")  #statements

# else:
#     print("statement is false")


# if(a>0):
#     print("greater than zero")

# elif(a<0):
#     print("less tham zero")

# else:
#     print("equal to zero")



#iteartors:

#2 diff types of loops: entry controlled(for,while), exit controlled (do while)


#python:

# i=1

# while(i<=10):
#     print(i)
#     i=i+1


# for i in range(10,0,-1):
#     print(i)

# for i in range(1,10,3):
#     print("*" * i)


#brak,continue,pass

# for i in range(1,11):
#     if (i>5):
#         break
#     print(i)


# for i in range(1,11):
#     if (i==5):
#         continue
#     print(i)


#pass:empty statement

#function:
#collection of statements used to perform some sppecific task

#adv:code reusability

#function is declared using "def" keyword

# def fun():
#     # print("this is function")
#     pass

# fun() #function calling

#argument,parameter

# def fun(a): #parameter:the value we passes through an argument
#     print(a)


# fun(10)  #argument:argument is the one which holds the parameter



#positional argument

# def fun(a,b):
#     print(a+b)


# fun(1,2)

#default argument

# def fun(a,b=5):
#     print(a+b)

# fun(1) #6
# fun(2,2) #4


#named argument

# def fun(a,b):
#     print(a+b)

# fun(b=5,a=10)

#arbitrary argument

# def fun(*a):
#     # print(a[1])
#     for i in a:
#         print(i)


# fun(1,2,3,4,5,6,7,8,9)


#keyword argument:

# def fun(fname,lname,year):
#      print(fname,lname,year)


# fun(fname="big",lname="query",year=2000)


#kw arbitrary argument

# def fun(**kw):
#     #  print(kw['fname'],kw['lname'])
#     for i,j in kw.items():
#         print(f'key is:{i} value is {j}')


# fun(fname="big",lname="query",year=2000)


#non premitive/collections
# list :mutable
# set  :mutable
# tuple : immutable
# dictionary :mutable

#all collection types are iterable

#list:
#it accepts duplicates
#it accepts multiple diff data types(used to store homogeneous data type)
#list is ordered
#we can add/remove/modify the values
#index based
#annotation = []

# lst=[1,1,2,2,3,4,5,6,2.3,False,'sql']
# print(type(lst))
# print(lst)


#methods

# lst=[1,2,3]

#append
# lst.append(4)
# print(lst)

#pop
# lst.pop()
# print(lst)

# lst.pop(0)
# print(lst)

#copy,clear
# lst.clear()
# print(lst)

# lst1=lst.copy()
# print(lst1)

#count
# print(lst.count(2))

#remove
# lst.remove(3)
# print(lst)

# lst.reverse()
# print(lst)

# lst.sort(reverse=True)
# print(lst)

#insert

# lst.insert(0,9)
# print(lst)

#index
# print(lst.index(2))

# lst1=[1,2,3]
# lst2=[4,5,6]

# lst1.extend(lst2)
# print(lst1)

#tuple:
#immutable
#multiple diff data types
#we can not perform inser/update/delete
#annotation :()

# tp=(1,2,3,4,5)
# print(len(tp))
# print(min(tp))
# print(max(tp))
# print(tp.index(5))

#type conversion

# lt=list(tp)
# lt.append(6)

# tp1=tuple(lt)
# print(tp1)

# tp1=(1,2)
# tp2=(3,4)
# print(tp1+tp2)

#unpacking tuples

# tp1=("red","green","blue")

# (color1,color2,color3)=tp1

# print(color1,color2,color3)



#set
#mutable 
#does not accepts duplicate values
#not index based
#un ordered
#we can insert,remove the values from list
#annotation:{}


# st={1,1,2,3,3,4,5}
# print(st)

#methods

# st={1,2,3,4}
# st.add(0)
# print(st)

#pop
# st.pop()
# print(st)
# st.pop(2)

# st1={"one",2,1,4}

#remove
# st.remove(5)
# print(st)

#discard:
# st.discard(5)
# print(st)

#extend

# st1={1,2,3}
# st2={4,5,6}
# st1.update(st2)
# print(st1)

#union
# st3=st1.union(st2)
# print(st3)

#isdisjoin
# st1={1,2,3}
# st2={4,5,6,1}
# print(st1.isdisjoint(st2))

#intersection

# st1={1,2,3}
# st2={4,5,6,1}

# print(st1.intersection(st2))
# print(st1.difference(st2))

#dictionary:
#collection of key and value pair
#key is unique(it does not accept duplicates)
#key is always enclosed with double quote
#we can update and remove the values from the dictionary
#annotation :{}

dt={"fname":"data","lname":"bricks","year":2001}
# print(dt["fname"])

# print(dt.get('loc','np'))
#clear,copy

# dt.pop("fname")
# print(dt)

# print(dt.keys())
# print(dt.values())
# print(dt.items())

#ierate

# for i,j in dt.items():
#     print(f'key is:{i} value is:{j}')

#update

# dt1={"fname":"usa"}
# dt.update(dt1)
# print(dt)


#string:
#collection of charcters which is enclosed by double/single quote

# str="databricks"
# st="DATABRICKS"
# s="369"
# print(str[-1])
# print(str.capitalize())
# print(str.upper())
# print(st.lower())
# print(str.isupper())
# print(str.islower())
# print(str.title())
# print(str.isalnum())
# print(str.isalpha())
# print(s.isnumeric())

# a=str.split('a')
# print(a)


#slicing

# lst=[1,2,3,4,5,6,7,8,9]
# [start:stop:step]
# print(lst[0:3])
# print(lst[:3])
# print(lst[3:])
# print(lst[::2])
# print(lst[-1])
# print(lst[-1:-3:-1])
# str="databricks"
# print(str[::-1])


# modular programming

# from md import *
# from md import add
# import md
# import md as m

# m.add(1,2)

#math

# import math

# print(math.floor(10.9))
# print(math.ceil(10.1))


#file handling:
#create  --> x
#write
#read
#append
#remove

# f=open('demo.txt','x')
# print('file created')

#write
# f=open('demo.txt','w')
# f.write('welcome to python!!!')
# f.close()

#read
# f=open('demo.txt','r')
# print(f.read())
# f.close()

#append
# f=open('demo.txt','a')
# f.write('\n')
# f.write("Hello!!!")
# f.close()

#remove
# import os
# os.remove('demo.txt')
# print("removed")

#exception handling

#error : error occurs at the time of program compile state
#exception : occurs at the time of program execution


#an un expected error occurs at the time of program execution

#blocks: try,except,finally

#try: program what we want to execute
#except : captures the exception
#finally block: irrespective of exception finally block always executes


# print(10+"sql")

# try:
#    print("sql")
# except Exception as e:
#    print("something wrong",e)
# except TypeError as e:
#    print(e)
# except Exception as e:
#    print(e)

# finally:
#    print("finally block always executes")




#oops (object oriented programming)

#object:
#    instance of class
#    anything which is physically presents consider to be an object
# object has state and behaviour
# state:
#     property to describe an object
# behaviour:
#     action performed by an object

# ex: laptop
# state: programmatically state of an object is called variable
#     color=black
#     model=asus
#     ram=16g  

#behaviour: programmatically behaviour of an object is called method
#   mailsend,pptcreation



#class:
#logical entity or blue print using which we can create an object
#class declared using class keyword

#step 1: create class
#step 2: create object

#class name should follow PascalCase

# class Laptop():
#     model="asus" #variable/state

#     def mail(self): #behaviour/method
#         print("sending mail")
#         # print(self.model)
#     def painting(self):
#         print("painting")

# obj=Laptop() #object creation (loading class file from hdd memory to ram memory (class loading))
# obj.mail()
# obj.painting()
# print(obj.model)


#constructor:
#  constructor helps us to construct the class variable

#two types of constructor:
#   default constructor
#   parameterised constructor


#default constructor:
#   a constructor which does not takes any argument/parameter default constructor
#   used to assign default values to the class variable
# class Laptop():
#     def __init__(self):
#         self.model="Asus"   

# obj=Laptop()
# print(obj.model)


# obj1=Laptop()
# print(obj1.model)

# obj2=Laptop()
# print(obj2.model)

#parameterised constructor:

#a constructor which takes argument/parameter 
#used to assign dynamic values to the class variable
# class Laptop():
#     def __init__(self,x):
#         self.model=x   

# obj=Laptop("asus")
# print(obj.model)


# obj1=Laptop("lenovo")
# print(obj1.model)

# obj2=Laptop("hp")
# print(obj2.model)

#destructor:
#helps us to remove un used object from the memory

# class Laptop():
#     def __init__(self):
#         self.model="asus"  
#     def __del__(self):
#         pass

# obj=Laptop()
# print(obj.model)
