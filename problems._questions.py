
# Even_or_odd = int(input("Enter the number to check the Even or odd : "))

# if (Even_or_odd <=0):
#     print(f"{Even_or_odd} is less than or Equal to 0 number please Enter the number which is Greater than 0") 
# elif (Even_or_odd %2==0):
#     print(f"{Even_or_odd} is an Even number")
x#     print(f"{Even_or_odd} is an odd number")
#     ----------------------------------------------------------

# multiple = int(input("Enter the number you want to multiple num : "))

# for i in range (1,11) :
#     print(f"{i} x {multiple}= {i*multiple}")
# ------------------------------------------------------------

# # sum of natural numbers 

# n = 100
# sum_natural = n*(n+1)//2

# print(f"The {n} sum of number is {sum_natural}")

# --------------------------------------------------------------
# n = 10
# sum_natural = 0
# for i in range(1, n + 1):
#     sum_natural += i
# print(f"Sum: {sum_natural}")
# --------------------------------------------------------------------
# add two numbers
# num1 = float(input("Enter the Value 1 : "))
# num2 = float(input("Enter the Value 2 : "))
# sum_output = num1+num2
# print(f"The addition of {num1} + {num2} is : {sum_output} ")
# ------------------------------------------------------------------------------
# division

# div1 = float(input("Enter the value for Dividend for Divison : "))
# div2 = float(input("Enter the value for Divisior for Division : "))
# if div2==0:
#     print("Error The divisor  should Greator than 0 ")
# else:
#     div_result = div1/div2
#     print(f"The divison of {div1} by {div2} is {div_result}")
# -----------------------------------------------------------------------------------------------

# Area of the rectangle

# base = float(input("Enter the length of the base  of triangle : "))
# Height  = float(input("Enter the length of the height  of triangle : "))

# area  = 0.5*base*Height

# print(f"The area of the rectangle is {area}")
# ----------------------------------------------------------------------------------------
# random number
# import random
# print(f"random number : {random.randint(1,100)}")
# ------------------------------------------------------------------------------------

# miles to kilometers conversion

# kilometer = float(input("Enter the distance in kilometer : "))

# conversion_factor = 0.621371

# miles = kilometer* conversion_factor
# print(f"{kilometer} is equal to {miles} miles")
# -----------------------------------------------------------------

# import calendar

# year = int(input("Enter the year : "))
# month = int(input("Enter the month : "))

# cal = calendar.month(year,month)
# print(cal)

#swap two variables 


#there is lot of method in it 

#using temp variable  Using a Temporary Variable (Traditional Way)

# a = 22
# b =20 

# print(f"The value before  the swap of a is {a} and the value of b is {b}")
# temp =a #10
# a =b #20
# b =temp #10

# print(f"The value after the swap of a is {a} and the value of b is {b}")

#asssinging method Python's Tuple Unpacking (Most Pythonic)

# a ,b = b,a

# print(f"The value after the swap of a is {a} and the value of b is {b}")


#  using Arthmetic operations

# a = a+b # 10+20 = 30
# b = a-b # 30-20 = 10
# a = a-b # 30 - 10 =20

# print(f"The value after the swap of a is {a} and the value of b is {b}")

# ------------------------------------------------------------------------------

# sum of the digits

# n =12341
# sum_of_digits = sum(int(digit) for digit in str(n))
# print(f"The sum of  {n} is {sum_of_digits}")
# --------------------------------------------------------------

# Reverse a string using inbulit method
 
# string = "praveen"

# print(string[::-1])

# for i in reversed(string) :
#     print(i)
# ------------------------------------------------

# s = "string_function"
# reversed_s = ""
# for i in range(len(s)-1,-1,-1):
#     reversed_s+=s[i]
# print(reversed_s)
# ------------------------------------------------------------

# counting vowles 

# vowles = ["a","e","i","o","u"]
# word = input(" Enter the word the find the vowles : ")
# count = 0 
# for characther in word.lower() :
#     if characther in  vowles  :
#         count+=1
# print(f"The word {word} consist of {count} vowels letter")
# -----------------------------------------------------------------------

# counting the number of occrancess of a charcther in a string 

# string =input("Enter the only word to count : ")
# char = input("Enter the letter to count : ")
# count = 0 
# for i in string:
#     if i ==char:
#         count+=1
# print(f" The letter {char} is appear {count}  in the word")

# ------------------------------------------------------------------------

# checking the palindrome using inbulit funtion

# word = input ("Enter the word to check if the word is palindrome : ").lower()

# if word==word[::-1]:
#     print(f"The {word} is palindrome")
# else:
#     print(f" The {word} is not an palindrome "

number = '12345'
if number == 12345 :
    print("is correct")
else :
    print("is wrong")
