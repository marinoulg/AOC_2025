def answer_part2(text_file="day_1.txt"):
    where_we_at = 50
    maxi = 100
    count_zeros = 0

    my_input = open(text_file, "r").read()
    updated_input = my_input.split("\n")

    for elem in updated_input:
        if elem.startswith("L"):
            if where_we_at == 0:
                where_we_at = 100

            new = (elem.replace("L", ""))
            if len(new)>2:
                new = int(new[-2:])

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
                where_we_at = updated_start


        elif elem.startswith("R"):
            if where_we_at == 100:
                where_we_at = 0

            new = (elem.replace("R", ""))
            if len(new) > 2:
                new = int(new[-2:])

                nb_of_rotations = int(elem[1:-2])
                count_zeros += nb_of_rotations
            else:
                new = int(new)

            updated_start = where_we_at + new

            if updated_start > 100:
                count_zeros += 1
                where_we_at = updated_start - maxi
            elif updated_start == 0 or updated_start == 100:
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


    print("count zeros:", count_zeros)

answer_part2()
