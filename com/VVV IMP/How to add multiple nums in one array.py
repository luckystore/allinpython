# How to Add multiple Nums in array
def Add_Number(*num):
    total = 0
    for i in num:
        total += i
    print(total)
Add_Number(12, 34, 56, 78)
Add_Number(755, 6535, 8765, 6, 653)
Add_Number(974, 23, 5754, 954, 42, 2, 1)

# Model2:
number = [12, 34, 56, 78]
total = 0
for i in number:
    total += i
print(total)