def get_ranges(text_file="example_day_5.txt"):
    """
    get the ranges in the text_file
    """
    my_input = open(text_file, "r").read()
    new = my_input.split("\n")

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

    return ranges_, list_2

def part_1(text_file="example_day_5.txt"):
    """
    Count the number of ingredients that are spoiled, aka NOT fresh.
    """
    ranges_, list_2 = get_ranges(text_file)
    count = 0
    for num in list_2:
        count_tmp = 0
        for ranges in ranges_:
            if int(num) < ranges[0] or int(num) > ranges[1]:
                count_tmp += 1
        if count_tmp == len(ranges_):
            count += 1

    print("total count of FRESH is: ", (len(list_2))-count)
    return len(list_2)-count

# print(part_1("day_5.txt"))

# ---------------- Part 2 ----------------


def get_new_range(tuple1, tuple2):
    """
    this function returns the correct range, if given two tuples

    need to implement options 9 and 10 for it to be complete (bc they happen in real input)
    """
    a,b = tuple1
    c,d = tuple2

    if a == c:
        # Option 4 or Option 6 or Option 8
        if d > b:
            # Option 6
            # a ------- b
            # c ------------- d
            new_range = (a,d)
            to_pop = [(a,b),(c,d)]

        elif d == b:
            # Option 4
            # a ------- b
            # c ------- d
            new_range = (a,b)
            to_pop = [(None, None)]
        elif d < b:
            # Option 8
            # a ------- b
            # c --- d
            new_range = (a,b)
            to_pop = [(c,d)]
        elif a == d:
            # Option 9
            # a ------- b
            # c
            # d
            new_range = (a,b)
            to_pop = [(c,d)]

    elif a < c:
        # Option 1 or Option 2 or Option 3 or Option 7
        if c < b and b < d:
            # Option 1
            # a ------- b
            #       c ------- d
            # print("option 1")
            new_range = (a,d)
            to_pop = [(a,b),(c,d)]
        elif c < b and d < b:
            # Option 2
            # a ------- b
            #   c -- d
            new_range = (a,b)
            to_pop = [(c,d)]
        elif c == b and b < d:
            # Option 3
            # a ------- b
                    #   c ---- d
            new_range = (a,d)
            to_pop = [(a,b),(c,d)]
        elif c < b and b == d:
            # Option 7
            # a ------- b
            #     c --- d
            new_range = (a,b)
            to_pop = [(c,d)]
        elif c == b and c == d:
            # Option 10
            # a ------- b
                    #   c
                    #   d
            new_range = (a,b)
            to_pop = [(c,d)]

        elif b < c:
            # Option 5 will be delt with on its own
            # a ------- b
            #               c ------- d
            new_range = ((a,b),(c,d))
            to_pop = [(None, None)]

    else:
        # it means that a > c, which is algorithmically the same as a < c, if a is c and c is a
        return get_new_range(tuple2, tuple1)

    return new_range, to_pop


def new_sets(ranges):

    """
    il pop pas option 7,
    et option 10 à rajouter pour le to_remove

    j'aime pas bcp ma manière de traiter le to_remove, à tweaker mieux je pense
    """

    new_list = set()
    ranges = sorted(ranges)
    to_remove = list()

    for j in range(len(ranges)):
        comparing = ranges[j]
        for i in range(len(ranges)):
            # print("comparing",(comparing, ranges[i]))
            if i != j:
                try:
                    n, to_pop = get_new_range(ranges[i], comparing)
                    if isinstance(n[0], int):
                        # print("+1")
                        # print("n",n)
                        for idx in range(len(to_pop)):
                            to_remove.append(to_pop[idx])
                            if to_pop[idx] in new_list:
                                new_list.remove(to_pop[idx])
                        new_list.add(n)
                        n_bis, to_pop = get_new_range(ranges[i], comparing)
                        if isinstance(n_bis[0], int):
                            for idx in range(len(to_pop)):
                                to_remove.append(to_pop[idx])
                                if to_pop[idx] in new_list:
                                    new_list.remove(to_pop[idx])
                            # print("comparing nbis",(n_bis, ranges[i]))
                            # print("+1")
                            # print("n",n)

                            new_list.add(n_bis)
                    else:
                        i += 1
                        # print(comparing)
                        # print("ok", tuple(ranges[i]))
                        # new_list.add(tuple(ranges[i]))
                        # print(comparing)
                        new_list.add(tuple(comparing))

                except UnboundLocalError:
                    i += 1
            else:
                # print("not together:", (tuple(comparing), tuple(ranges[i])))
                pass

    # for idx in range(len(to_remove)):
    #     print(to_pop[idx])
    #     if to_pop[idx] in new_list:
    #         new_list.remove(to_pop[idx])
    new_list = sorted(list(new_list))

    to_remove = (list(set(to_remove)))
    for i in range(len(to_remove)):
        a,b = to_remove[i]
        if (a,b) in new_list:
            new_list.remove((a,b))


    return new_list, to_remove


def get_answer(text_file="example_day_5.txt"):
    ranges = get_ranges(text_file)[0]
    new_list = ranges.copy()
    iteration = 4

    my_dict = {0:0, 1:1, 2:2, 3:3, 4:4}
    for _ in range(100000):
        new_list = new_sets(new_list)[0]
        print(new_list)
        my_dict[iteration] = (new_list)

        if my_dict[iteration] == my_dict[iteration-1] == my_dict[iteration-2] == my_dict[iteration-3] == my_dict[iteration-4]:
            print("iteration:", iteration-1)
            break
        iteration += 1
    else:
        print(iteration)

    return my_dict, iteration



def return_part1(file_text="day_5.txt"):
    dict_, iteration = get_answer(file_text)
    answer = list(dict_[iteration])

    total = list()
    for i in range(len(answer)):
        a,b = answer[i]
        # print((b+1)-a)
        total.append((b+1)-a)

    return sum(total)





# 372759287730410
# 370192515053777
# 370 192 515 053 777
# 369 993 886 244 502

# is too high

# 344 322 275 609 331 not the right answer
# 344 322 275 609 198 not the right answer
# 344 322 275 609 331

# il faut tweeker le code pour sort by col "1" en ordonné aussi
# 344123646800056
# 304 381 322 684 534 not the correct answer
# 304 381 322 684 534
# 353 376 608 341 030
# 387 392 299 327 819
