# my_input = open("example_day_3.txt", "r").read()

# updated_input = my_input.split("\n") #[176:178]
# print(updated_input)

def find_elem(elem, str_to_be_found):
    """
    mon problème vient d'ici parce que parfois il retourne des None
    --> quand ma str_to_be_found n'existe pas dans la chaîne de characters

    de plus, il ne détecte pas le dernier caractère de elem
    """
    # print(range(len(elem)))
    # breakpoint()
    for i in range(len(elem)):
        if elem[i] == str_to_be_found:
            # print("elem updated:", elem.replace(elem[i], "", 1))
            print(f"position of {elem[i]}:", i)
            reminder = (len(elem)-i)
            # print("reminder after this character:",reminder)
            print("True")
            if reminder != 0:
                return elem[i+1:], reminder
            else:
                print("here")
                return str(), reminder
        else:
            print(f"{str_to_be_found} cannot be found in {elem}")
            next
            return 0

def find_biggest_two(elem):
    """
    default value : elem = updated_input[0]
    """
    first_line = []

    for num in range(9, -1, -1):
        if str(num) in elem:
            new_elem, reminder = find_elem(elem,
                    str(num))

            if len(new_elem) > 0:
                first_line.append(str(num))
                for i in range(9, -1, -1):
                    # second_iteration, reminder =
                    if find_elem(new_elem, str(i)) != None:
                        first_line.append(str(i))
            else:
                next

    return int(first_line[0]+first_line[1])

def result_1(text_file = "example_day_3.txt"):
    my_input = open(text_file, "r").read()

    updated_input = my_input.split("\n") #[176:178]

    result_p1 = list()
    for i in range(len(updated_input)-1):
        result_p1.append((find_biggest_two(updated_input[i])))
        print()

    # print((result_p1))
    return (sum(result_p1))

# print(result_1())


# ------------ Part 2 ------------
# test = updated_input[0]
# print(type(test), test)


my_input = open("example_day_3.txt", "r").read()

updated_input = my_input.split("\n") #[176:178]



elem = updated_input[1]
print(elem)
print(elem[14])

# a, rem = find_elem(elem, "9")
# print(a)
# print(rem)


biggest_12_digits = []

biggest = 9
nb_of_digits_left_to_find = 10 # bigger than 10 means at least 11 characters, to which we had the first one (just found) --> 12 digits

str_to_be_found=str(biggest)
new_elem, reminder = (find_elem(elem, str_to_be_found))

if reminder > nb_of_digits_left_to_find:
    print("found element:", str_to_be_found)
    print("reminder characters are:", new_elem)
    print("reminder nb of char:", reminder)
    biggest_12_digits.append(str_to_be_found)

else:
    str_to_be_found=str(biggest - 1)
    new_elem, reminder = (find_elem(elem, str_to_be_found))

    print("found element:", str_to_be_found)
    print("reminder characters are:", new_elem)
    print("reminder nb of char:", reminder)
    biggest_12_digits.append(str_to_be_found)




# print(biggest_12_digits)
# print("new_elem:", new_elem)

# breakpoint()
new_elem = updated_input[1]

"""
list_to_be_browsed_through = []
for i in range(9,-1,-1):
    list_to_be_browsed_through.append(str(i))

# print(list_to_be_browsed_through)

for i in list_to_be_browsed_through:
    # print(i)
    try:
        str_to_be_found = str(i)
        new_elem, reminder = find_elem(new_elem, i)
        print("new_elem:", new_elem)
        print("reminder nb of char:", reminder)

        # if str(i) in new_elem:
        if reminder > nb_of_digits_left_to_find:
            print("found element:", str_to_be_found)
            print("reminder characters are:", new_elem)
            print("reminder nb of char:", reminder)
            biggest_12_digits.append(str_to_be_found)
            nb_of_digits_left_to_find = nb_of_digits_left_to_find - 1
    except TypeError:
        print("TypeError for:", i)
    print("new_elem:", new_elem)
        # next
    print()
    #

print(biggest_12_digits)
"""


def test_len_and_possibility(test, length_next=10):
    """
    Je teste s'il y a un 9 d'abord et si la suite de nombres (format string)
    est supérieure à 10 (donc 11 ou plus chiffres/caractères ensuite).

    comme parfois t peut être égal à None, ensuite ça bloque toute la chaîne.
    """
    list_to_be_browsed_through = []
    for i in range(9,-1,-1):
        list_to_be_browsed_through.append(str(i))

    for i in list_to_be_browsed_through:
        t, reminder = (find_elem(test, str_to_be_found=f"{i}"))
        if t != None:
            # print(len(t))
            # print(t)
            if reminder > length_next:
                # print("possible")
                return i, t
        # else:
        #     return -1

# i, t = test_len_and_possibility(new_elem, 10)
# print(i, t)

def for_one_elem_in_list(test):
    biggest_num = []
    for idx in range(10, -1, -1):
        try:
            i, test = (test_len_and_possibility(test, idx))
            # print(test)
            # print("normal sc. i: ", i)
            # print("test:", test)
            # print()
            biggest_num.append(i)
            if idx == 0:
                # print("test:", test)
                # print("idx0 sc. i: ", max(test))
                biggest_num.append(int(max(test)))
                return test, biggest_num
        except TypeError:
            print()
            # print(len(biggest_num))
            print(len(test))
            print(test, type(test))
            # while len(biggest_num) < 12:
            #     missing = 12-len(biggest_num)
            #     print("missing", missing)
            for j in range(len(test)):
                # print("j", j)
                i, test = test_len_and_possibility(test, missing-j)
                # print("typeerror sc. i: ", i)
                # print("test:", test)
                """
                ces deux lignes ne veulent pas marcher !!
                """
                if len(biggest_num) > 11:
                    break
            for i in test:
                # print("typeerror sc. i: ", i)
                # print("test:", test)
                biggest_num.append(i)
            # return test, biggest_num
        # biggest_num+=str(i)

    # print(biggest_num[:12])
    return (biggest_num) #[:12])

# biggest_num = for_one_elem_in_list(test)
# print(biggest_num, ", ", len(biggest_num))

# # test = "7769"
# # for j in range(len(test)):
# #     i, test = (test_len_and_possibility(test, missing))
# #     print("i:", i)
# #     print("t:", test)



# print("typeerror sc. i: ", i)
# print("test:", test)
missing = 2
k = 8


# test, big = for_one_elem_in_list(test)
# print("test", test)
# print("big", big)
# find = find_elem(test, f"{k}")
# # print("find elem", (find))
# idx = (len(test)-len(find_elem(test, f"{k}")))-1
# print(idx, test[idx])
# print("test", test)


# print("end:", test_len_and_possibility(test, missing-1))
# print("i:", i)
# print("t:", t)


def get_result(updated_input):
    big_nums = []
    for i in range(len(updated_input)-1):
        test = updated_input[i]
        big = for_one_elem_in_list(test)
        # print((big))
        biggest = str()
        for j in big:
            biggest+=str(j)
            print(biggest)
            big_nums.append(int(biggest))
    print(i, ",", int(biggest), ", ", len(biggest))
        # print("-"*10)
        # print()

    print()
    print(sum(big_nums))

# get_result(updated_input)

# 979 335 968 934 983 710 995 866 too high
# 102 781 982 770 870 is too low
# 168 798 209 055 492 is too low


# 987654321111 / 987654321111
# 811111111119 / 811111111119
# 434234234278 / 43423423427
# 888911112111 / 888911112111

# 3121910778619 / 3121910778619
