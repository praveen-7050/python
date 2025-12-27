
'''
num = 11
if(num%2==0):
    print("even number")
else :
    print("odd number")


age =45

if(age>1 and age<=2):
    print("child")
elif(age>2 and age <=10):
    print("infant")
elif(age>10 and age <=18):
    print("teen")
elif(age>18 and age <=35):
    print("adult")
elif (age>35 and age <=56):
    print("uncle")
elif(age>50 and age <=100):
    print("senior citizen")

fb = 15

if(fb%3==0 and fb%5==0):
    print("fizz and buzz")
elif(fb%3==0):
    print("fizz")
elif(fb%5==0):
    print("Buzz")

number = -10

if(number>0):
    print("postive number")
elif(number==0):
    print("netural number")
elif(number<0):
    print("negative number")


unit = 150
totalbill = 0 
if(unit>0 and unit <=100):
    print("free")
elif(unit > 100 and unit <=250):
    totalbill = (unit-100)*3
    print('totalbill is ',totalbill)
elif(unit>250 and unit <= 350) :
    totalbill = ((100*3)+(unit-200)*5)
    print('totalbill is ',totalbill)
elif(unit>350 and unit <= 500):
     totalbill=((100*3)+(100*5)+(unit-300)*6)
     print('totalbill is ',totalbill)
else :
     print('above the limit ')
     '''
color = "Green"
if(color=="Red"):
     print("Stop")
elif(color=="Orange"):
     print("Wait")
elif(color == "Green"):
    print("Go")
else:
     print("Not a siginal Color")


age = 12
citizen = "indian"

if(age >=18 and citizen == "indian"):
     print("You are elgible to vote")
elif(age<=18 and citizen == "indian") or (age>=18 and  citizen != "indian"):
     print("you are not elgible to vote ")
else:
     print("invalid age number and invalid citieznhip not in the world")


vowles = "a";

if(vowles in ['a','e','i','o','u']):
     print("it include vowles")
else:
     print("it's not a vowles")


personAge= 30
citizen = "Indn"

if(personAge >= 18 ):
    if(citizen=='Indian'):
         print("You are elgible for drive the vechile")
    else:
         print('you are not citizen of indian so you are not allowed to drive')
else:
     print("you are not elgible get the linces")
         
leap_Year = 2004

if(leap_Year% 400==0 and leap_Year%4==0)or(leap_Year%100==0):
     print(f"The {leap_Year} is a Leap year")
else:
     print(f"This {leap_Year} is not a leap year")