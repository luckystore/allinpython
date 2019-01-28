print("------Model 1------")
# model 1
x = 'KHgffdREJdgE'
print('Capital Letter:', sum(1 for c in x if c.isupper()))
print("------Model 2------")
# model 2
count = 0
for char in x:
    if char.isupper():
        count += 1
print(count)
print("------Model 3------")
# model 3
for i in x:
    if i.isupper():
        print(i)