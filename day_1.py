where_we_at = 50

maxi = 100
mini = 0

my_input = open("my_test_day_1.txt", "r").read()

updated_input = my_input.split("\n")
# print(updated_input[:3])


count_zeros = 0

print("Start:", where_we_at)
print()

for elem in updated_input:
    if elem.startswith("L"):
        if where_we_at == 0:
            where_we_at=100

        print(elem)
        new = (elem.replace("L", ""))
        if len(new)>2:
            new = int(new[-2:])
            print(elem[1:-2])

            nb_of_rotations = int(elem[1:-2])
            count_zeros += nb_of_rotations
        else:
            new = int(new)

        updated_start = where_we_at - new

        if updated_start < 0:
            count_zeros += 1
            where_we_at = maxi - abs(updated_start)
        elif updated_start == 0 or updated_start==100:
            count_zeros += 1
            where_we_at = 100
        else:
            where_we_at=updated_start


    elif elem.startswith("R"):
        if where_we_at == 100:
            where_we_at=0

        print(elem)
        new = (elem.replace("R", ""))
        if len(new)>2:
            new = int(new[-2:])
            print(elem[1:-2])

            nb_of_rotations = int(elem[1:-2])
            count_zeros += nb_of_rotations
        else:
            new = int(new)

        updated_start = where_we_at + new

        if updated_start > 100:
            count_zeros += 1
            where_we_at = updated_start - maxi
        elif updated_start == 0 or updated_start==100:
            count_zeros += 1
            where_we_at = 100
        else:
            where_we_at=updated_start

    elif where_we_at > 100:
        where_we_at = int(str(where_we_at)[-2:])

        nb_of_rotations = int(str(where_we_at)[:-2])
        count_zeros += nb_of_rotations

    elif where_we_at < -100:
        where_we_at = int(str(where_we_at)[-2:])
        where_we_at = maxi - abs(where_we_at)

        nb_of_rotations = int(str(where_we_at)[:-2])
        count_zeros += nb_of_rotations

    print("where we at:", where_we_at)
    print("count zeros:", count_zeros)
    print()


print("count zeros:", count_zeros)

# Part 1
# Answer is 982

# Part 2
# Answer is 6106
