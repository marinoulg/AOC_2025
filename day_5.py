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

    to_return = list()

    if a == c:
        # Option 4 or Option 6 or Option 8
        if d > b:
            # Option 6
            # a ------- b
            # c ------------- d
            new_range = (a,d)
            # to_pop = [(a,b),(c,d)]

        elif d == b:
            # Option 4
            # a ------- b
            # c ------- d
            new_range = (a,b)
        elif d < b:
            # Option 8
            # a ------- b
            # c --- d
            new_range = (a,b)
        elif a == d:
            # Option 9
            # a ------- b
            # c
            # d
            new_range = (a,b)

    elif a < c:
        # Option 1 or Option 2 or Option 3 or Option 7
        if c < b and b < d:
            # Option 1
            # a ------- b
            #       c ------- d
            # print("option 1")
            new_range = (a,d)
            # to_pop = [(a,b),(c,d)]
        elif c < b and d < b:
            # Option 2
            # a ------- b
            #   c -- d
            new_range = (a,b)
        elif c == b and b < d:
            # Option 3
            # a ------- b
                    #   c ---- d
            new_range = (a,d)
        elif c < b and b == d:
            # Option 7
            # a ------- b
            #     c --- d
            new_range = (a,b)
        elif c == b and c == d:
            # Option 10
            # a ------- b
                    #   c
                    #   d
            new_range = (a,b)
        elif b+1 < c:
            # Option 5 will be delt with on its own
            # a ------- b
            #               c ------- d
            new_range = ((c,d))
            to_return.append((a,b))
        elif c == (b+1):
            new_range = (a,d)

    else:
        # it means that a > c, which is algorithmically the same as a < c, if a is c and c is a
        return get_new_range(tuple2, tuple1)

    return new_range


def get_all_ranges(text_file="example_day_5.txt"):

    ranges, list_2 = get_ranges(text_file)

    ranges = sorted(ranges)
    new_range = tuple(ranges[0])

    to_be_returned = list()

    if len(ranges) > 1:
        for idx in range(1, len(ranges)):
            old_range = new_range
            new_range = get_new_range(new_range, ranges[idx])
            if old_range[1] < new_range[0]:
                to_be_returned.append(old_range)

        new_range = get_new_range(new_range, ranges[idx])
        if old_range[1] < new_range[0]:
            to_be_returned.append(new_range)

        new_range = (get_new_range(old_range, new_range))
        if new_range not in to_be_returned:
            to_be_returned.append(new_range)
    else:
        return tuple(ranges[0])

    return to_be_returned


def answer_part2(text_file="example_day_5.txt"):
    my_liste = get_all_ranges(text_file)

    total = list()
    for i in range(len(my_liste)):
        a,b = my_liste[i]
        total.append((b+1)-a)

    return (sum(total))

print(answer_part2("day_5.txt"))
