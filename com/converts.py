# Convert string to list
def convert(string):
    item = list(string.split())
    return item
str = "Write a program "
print(convert(str))

# Convert list to dictionary
str = ['write', 'a', 'program']
my_dict = {}
i = 1
for i in range(3):
    my_dict[str[i]] = str[i]
print(my_dict)

# Convert dictionary to tuple
d = my_dict
keys = d.keys()
values = d.values()
print(tuple(keys))

# Convert tuple to string
a = ('write', 'a', 'program')
string = ' '.join(a)
print(string)
