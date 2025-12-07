import pandas as pd

my_input = open("day_5.txt", "r").read()
new = my_input.split("\n")
# print(new)

list_1=list()
list_2 = list()
for i in range(len((new))):
    if new[i] != '':
        list_1.append(new[i])
    else:
        for idx in range(i+1, len((new))-1):
            list_2.append(new[idx])
        break

ranges_ = []
for idx in range(len(list_1)):
    a, b = list_1[idx].split("-")
    ranges_.append([int(a), int(b)])

print(ranges_)

count = 0

# Count the number of ingredients that are spoiled, aka NOT fresh
for num in list_2:
    count_tmp = 0
    for ranges in ranges_:
        if int(num) < ranges[0] or int(num) > ranges[1]:
            count_tmp += 1
    if count_tmp == len(ranges_):
        print(f"{num} not in any ranges")
        count += 1


print("total count of spoiled is: ", count)
print()
print("total count of FRESH is: ", (len(list_2))-count)
