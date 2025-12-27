# names = ["praveen","surya","tharun","premkesh","mani","srikanth","kishore"]

# for upper in names :
    # print(upper.upper())
'''
corrected_Pin = '1234'
Entered_Pin = ''
while corrected_Pin != Entered_Pin :
    Entered_Pin = input("enter your corrected pin ")
print('access granted')
'''
'''
for x in range(10,1):
    print(x)
    

arr = [1,2,3,4,5,6,7,8,9,10]

for inp in arr :
    if(inp==5):
        continue 
    print(inp)

'''
'''
n=[1,2,-3,-30,-20,20,-3,-4,6,79,3]

for num in n :
    if(num<0):
        pass
    print(num)
'''

'''
items =[]
while True :
    item=input("Enter the cart input : ")
    if(item.lower()=="done"):
        break
    print("item Added")
    items.append(item)
print("item in cart",items)
'''
'''
'''
#prime numbers
'''
num =17

for i in range (2,num):
    if num % i==0:
        print("not a prime")
        break
else:
    print("prime number",num)
'''

# for i in range(1,50):
#     if (i%2==0):
#         print("it is even number ",i)
#     else:
#         print("it is odd number ",i)
table=11
num = 5 
for i in range (1,table):
    print(f"{i}  x {num} = {i*num}")
    
number=10
fact =1
n=1
while(n<=number):
    fact=fact*n
    n=n+1
print(f"factorial of {number} is {fact}")

the_No = 1234
total =0
for i in range(1,n+1):
    total+=i
print(f"the sum of {the_No} is {total}")