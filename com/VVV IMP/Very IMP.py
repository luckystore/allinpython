# Python code to demonstrate
# *args for dynamic arguments
# Model 1
def fn(*argList):
    for argx in argList:
        print(argx)


fn('I', 'am', 'Learning', 'Python')
# Model 2
list_arg = ['I', 'am', 'Kiran']
for x in list_arg:
    print(x)

# PG 2
# Python code to demonstrate
# **kwargs for dynamic + named arguments
def fn1(**kwargs):
    for emp, age in kwargs.items():
        print("%s's age is %s." % (emp, age))

fn1(John=25, Kalley=22, Tom=32)

# PG 4
print("Welcome")
print("__name__ contains: ", __name__)
def main():
    print("Testing the main function")
if __name__ == '__main__':
    main()

# PG 5
print(ord("z"))

# PG 6
#Example
test_str = 'Programming    '
# The trailing whitespaces are excluded
print(test_str.rstrip())

# PG 7
#Example
str = 'pdf csv json'
print(str.split(" "))
print(str.split())

# PG 8
#Example
str = 'lEaRn pYtHoN'
print(str.title())

# PG 9
# Simple Python function
def fn():
    return "Simple Python function."

# Python Generator function
def generate():
    yield "Python Generator function."

print(next(generate()))

# PG 10
# Example - enumerate function
alist = ["apple", "mango", "orange"]
astr = "banana"

# Let's set the enumerate objects
list_obj = enumerate(alist)
str_obj = enumerate(astr)

print("list_obj type:", type(list_obj))
print("str_obj type:", type(str_obj))

print(list(enumerate(alist)))
# Move the starting index to two from zero
print(list(enumerate(astr, 2)))

# PG 11
# Model 1
def testgen(index):
  weekdays = ['sun','mon','tue','wed','thu','fri','sat']
  yield weekdays[index]
  yield weekdays[index+1]

day = testgen(0)
print(next(day), next(day))

# PG 12
# Model 2
def test(index):
    list = ['sun', 'mon', 'tus', 'wed', 'thu', 'fri', 'sat']
    day  = list[index]
    day1 = list[index+1]
    day2 = list[index+2]
    print(day, day1, day2)
test(0)
#output: sun mon

# PG 13
list = []
for num in range(1, 10):
    list.append(num)
    rev = list[::-1]
    print(rev)