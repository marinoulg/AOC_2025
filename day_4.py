import pandas as pd
from time import time

# --------------- Part 1 ---------------

def setup(text_file = "day_4.txt"):
    my_input = open(text_file, "r").read()
    new = my_input.split("\n")

    df = []
    for x in range(len(new)-1):
        temp = []
        for i in new[x]:
            temp.append(i)
        df.append(temp)

    df = (pd.DataFrame(df))
    return df


def get_coordinates(df):
    coordinates = []
    for idx in (range(df.shape[0])):
        for col in range(df.shape[1]):
            if df.loc[idx, col] == "@": # for answers
                coordinates.append((idx, col))
    return coordinates


def remove_forklifts(df):
    coordinates = get_coordinates(df)

    coords = {}
    for coordinate in coordinates:
        idx, col = coordinate
        count = 0

        if (idx+1, col) in coordinates:
            count+= 1
        if (idx+1, col+1) in coordinates:
            count+= 1
        if (idx+1, col-1) in coordinates:
            count+= 1

        if (idx-1, col-1) in coordinates:
            count+= 1
        if (idx-1, col) in coordinates:
            count+= 1
        if (idx-1, col+1) in coordinates:
            count+= 1

        if (idx, col+1) in coordinates:
            count+= 1
        if (idx, col-1) in coordinates:
            count+= 1

        coords[(idx, col)] = count


    to_be_removed = []
    count = 0
    for key in list(coords.keys()):
        if coords[key] < 4:
            count += 1
            to_be_removed.append(key)

    return coords, count, to_be_removed

def answer_part1(text_file = "day_4.txt"):
    df = setup(text_file)

    coords, count, to_be_removed = remove_forklifts(df)
    return count

print("Part 1:", answer_part1())



# --------------- Part 2 ---------------

def answer_part2(text_file = "day_4.txt"):
    now = time()
    df = setup(text_file)

    total = 0
    to_stop = 0

    for _ in range(10000):
        coords, count, to_be_removed = remove_forklifts(df)
        for key in list(to_be_removed):
            idx, col = key
            df.loc[idx, col] = '.'
        total += (count)

        if count == 0:
            to_stop += 1

        if to_stop == 5:
            end = time()
            break

    return total, (end-now)

total, secs = answer_part2()
print(f"Part 2: {total} in {secs} seconds")
