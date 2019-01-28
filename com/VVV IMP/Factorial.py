# Model 1:
def factorial_num(x):
    for j in range(1, x):
        if x % j == 0:
            print(j)
print(factorial_num(320))

# Doubt
# for x in range(320):
#     for i in range(1, x):
#         if x % i == 0:
#             print(i)
# Model 2:

# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# uncomment to take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)