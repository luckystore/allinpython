# Model 1
print('Model 1')
print('Even Numbers')
for i in range(20):
    if i % 2 == 0:
        print(i)
print('Odd Numbers')
for j in range(20):
    if j % 2 != 0:
        print(j)

#Model 2
print('Model 2')
list = list(range(20))
# Even Numbers
print(list[0::2])
# Odd Numbers
print(list[1::2])
# 3 Digits different like  1 4 7 10
print(list[1::3])

# Model 3
print('Model 3')
for i in range(1, 20, 2):
    print(i)

# for j in xrange(-1, -10, -2):
#     print(j)