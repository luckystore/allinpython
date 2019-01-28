# x = 10
# n1 = 0
# n2 = 1
# count = 0
# while count < x:
#     temp = n1 + n2
#     # update values
#     n1 = n2
#     n2 = temp
#     count += 1
#     print(n1, end=' , ')                            # That end attribute will change output cross line like 1,1,2,3,5,8

# Model 2
num1 = 0
num2 = 1
for i in range(1,11):
        temp1 = num1 + num2

        num1 = num2
        num2 = temp1

        print(num1)