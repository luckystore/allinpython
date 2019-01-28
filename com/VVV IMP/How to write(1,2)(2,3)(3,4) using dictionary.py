import operator
dict = {1:2, 3:4, 4:5, 6:7}
val = sorted(dict.items(), key=lambda x: x[1])
print(val)

# or
val2 = sorted(dict.items(), key=operator.itemgetter(1))
print(val2)