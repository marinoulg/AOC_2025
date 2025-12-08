my_input = open("example_day_3.txt", "r").read()

updated_input = my_input.split("\n") #[176:178]
# print(updated_input)

def find_elem(elem, str_to_be_found):
    """
    mon problème vient d'ici parce que parfois il retourne des None
    """
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

print((result_p1))
print(sum(result_p1))


# ------------ Part 2 ------------
# test = updated_input[0]
# print(type(test), test)


def test_len_and_possibility(test, length_next=10):
    # je teste s'il y a un 9 d'abord et si la suite est supérieure à 10 (donc 11 ou plus)
    """
    comme parfois t peut être égal à None, ensuite ça bloque toute la chaîne.
    """
    for i in range(len(test), -1, -1):
        t = (find_elem(test, str_to_be_found=f"{i}"))
        if t != None:
            # print(len(t))
            # print(t)
            if len(t) > length_next:
                # print("possible")
                return i, t
        # else:
        #     return -1


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

get_result(updated_input)

# 979 335 968 934 983 710 995 866 too high
# 102 781 982 770 870 is too low
# 168 798 209 055 492 is too low


# 987654321111 / 987654321111
# 811111111119 / 811111111119
# 434234234278 / 43423423427
# 888911112111 / 888911112111

# 3121910778619 / 3121910778619
