my_input = open("example_day_3.txt", "r").read()

updated_input = my_input.split("\n")
# print(updated_input)

def find_elem(elem, str_to_be_found):
    for i in range(len(elem)):
        if elem[i] == str_to_be_found:
            # print("elem updated:", elem.replace(elem[i], "", 1))
            # print(f"position of {elem[i]}:", i)
            # print("True")
            return elem[i+1:]

def find_biggest_two(elem = updated_input[0]):
    first_line = []

    for num in range(9, -1, -1):
        if str(num) in elem:
            new_elem = find_elem(elem,
                    str(num))

            if len(new_elem) > 0:
                first_line.append(str(num))
                for i in range(9, -1, -1):
                    if find_elem(new_elem, str(i)) != None:
                        first_line.append(str(i))
            else:
                next

    return int(first_line[0]+first_line[1])


result_p1 = list()
for i in range(len(updated_input)-1):
    result_p1.append((find_biggest_two(updated_input[i])))

# print(sum(result_p1))


def find_biggest_twelve(elem = updated_input[0], length=11):
    first_line = []

    for num in range(9, -1, -1):
        if str(num) in elem:
            new_elem = find_elem(elem,
                    str(num))

            if len(new_elem) > length:
                # print(max(new_elem))
                idx = new_elem.find(max(new_elem), len(new_elem))
                # print((new_elem[idx:]))
                if len((new_elem[idx:])) > (length-1):
                    first_line.append(max(new_elem))
                    print(first_line, new_elem)
                    return first_line, new_elem
                else:
                    first_line.append(max(str(num)))
                    print(first_line, new_elem)
                    return first_line, new_elem

            else:
                next



first_line, new_elem = find_biggest_twelve(elem = updated_input[2], length=12)
# print(first_line, new_elem)
print()
for i in range(11):
    first_line, new_elem = find_biggest_twelve(elem = new_elem, length=10-i)

# first_line, new_elem = find_biggest_twelve(elem = new_elem, length=8)


# for i in range(10):
#     first_line, new_elem = find_biggest_twelve(elem = new_elem, length=10-i)
#     print(first_line, new_elem)
#     print()


"""
it1 = find_biggest_twelve(elem = updated_input[1])
print(it1[0])

it2 = find_biggest_twelve(elem=it1, length=10)
print(it2[1])

it3 = find_biggest_twelve(elem=it2, length=9)
print(it3[2])

it4 = find_biggest_twelve(elem=it3, length=8)
print(it4[3])

it5 = find_biggest_twelve(elem=it4, length=7)
print(it5[4])

it6 = find_biggest_twelve(elem=it5, length=6)
print(it6[5])

it7 = find_biggest_twelve(elem=it6, length=5)
print(it7[6])

it8 = find_biggest_twelve(elem=it7, length=4)
print(it8[7])

it9 = find_biggest_twelve(elem=it8, length=3)
print(it9[8])

it10 = find_biggest_twelve(elem=it9, length=2)
print(it10[9])

it11 = find_biggest_twelve(elem=it10, length=1)
print(it11[10])

it12 = find_biggest_twelve(elem=it11, length=0)
print(it12[11])

print()
print(it12)
print(max(it12))
"""
