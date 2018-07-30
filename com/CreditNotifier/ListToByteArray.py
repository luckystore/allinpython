mylist = ['1', 'WellsForgo', 'Savings', '1', '3323232324', 'John', '$750 ', '1532490000000', '1532320000000', 'ECS']

print(mylist)
mybyteArry = bytearray()
for i in mylist:
    print(i)
    print(i.encode('utf-8'))
    print(bytearray.append(i.encode(),'utf-8'))