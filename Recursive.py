# A recursive function is functin calling itself to break a big problem into smaller,manageable until it stopping condition is hit.
# base case and recursive case
# n = input('Enter the number to be factorial : ') # no need
def fact(n):
    if n == 0 or n == 1 :
        return 1
    return n*fact(n-1)
print(fact(10))