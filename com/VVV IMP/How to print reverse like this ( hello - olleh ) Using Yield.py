# Model 1
str = 'hello'
rev = str[::-1]

for i in rev:
    print(i)
print(rev)

# Model 2
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, - 1, - 1):
        yield my_str[i]


for char in rev_str("hello"):
    print(char)
print('====')
# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h


# 2nd PG:
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
a = [x**2 for x in my_list]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
b = (x**2 for x in my_list)

print(a)
print(b)

# 3rd PG
# Intialize the list
# my_list2 = [1, 3, 6, 10]
#
# a2 = (x**2 for x in my_list2)
# # Output: 1
# print(next(a2))
#
# # Output: 9
# print(next(a2))
#
# # Output: 36
# print(next(a2))
#
# # Output: 100
# print(next(a2))
#
# # Output: StopIteration
# next(a2)