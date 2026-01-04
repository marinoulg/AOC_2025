# ------------- Part 1 -------------

def is_invalid_1(x):
    if len(str(x)) % 2 == 0:
            half = int(len(str(x))/2)

            first_half = str(x)[:half]
            last_half = str(x)[half:]
            if first_half == last_half:
                invalid_ID = int(first_half+last_half)
                return invalid_ID

def answer_part1(text_file="day_2.txt"):
    my_input = open(text_file, "r").read()
    updated_input = my_input.split(",")

    invalid_IDs = []
    for elem in updated_input:
        start, end = elem.split("-")
        start = int(start)
        end = int(end)

        for x in range(start, end+1):
            if is_invalid_1(x):
                invalid_ID = is_invalid_1(x)
                invalid_IDs.append(invalid_ID)
    return (sum(invalid_IDs))

print("Part 1:", answer_part1())

# ------------- Part 2 -------------

def is_invalid(x):
    if len(str(x)) % 2 == 0:
            half = int(len(str(x))/2)

            first_half = str(x)[:half]
            last_half = str(x)[half:]
            if first_half == last_half:
                invalid_ID = int(first_half+last_half)
                return invalid_ID

    if len(str(x)) % 3 == 0:
        div = int(len(str(x))/3)

        first_div = str(x)[:div]
        sec_div = str(x)[div:2*div]
        third_div = str(x)[2*div:]
        if first_div == sec_div == third_div:
            invalid_ID = int(first_div+sec_div+third_div)
            return invalid_ID

    if len(str(x)) % 5 == 0:
        div = int(len(str(x))/5)

        first_div = str(x)[:div]
        sec_div = str(x)[div:2*div]
        third_div = str(x)[2*div:3*div]
        fourth_div = str(x)[3*div:4*div]
        fifth_div = str(x)[4*div:]

        if first_div == sec_div == third_div == fourth_div == fifth_div:
            invalid_ID = int(first_div+sec_div+third_div+fourth_div+fifth_div)
            return invalid_ID

    if len(str(x)) % 7 == 0:
        div = int(len(str(x))/7)

        first_div = str(x)[:div]
        sec_div = str(x)[div:2*div]
        third_div = str(x)[2*div:3*div]
        fourth_div = str(x)[3*div:4*div]
        fifth_div = str(x)[4*div:5*div]
        sixth_div = str(x)[5*div:6*div]
        seventh_div = str(x)[6*div:]

        if first_div == sec_div == third_div == fourth_div == fifth_div == sixth_div == seventh_div:
            invalid_ID = int(first_div + sec_div + third_div + fourth_div + fifth_div + sixth_div + seventh_div)
            return invalid_ID

def answer_part2(text_file="day_2.txt"):
    my_input = open(text_file, "r").read()
    updated_input = my_input.split(",")

    invalid_IDs = []
    for elem in updated_input:
        start, end = elem.split("-")
        start = int(start)
        end = int(end)

        for x in range(start, end+1):
            if is_invalid(x):
                invalid_ID = is_invalid(x)
                invalid_IDs.append(invalid_ID)

    return (sum(invalid_IDs))

print("Part 2:", answer_part2())
