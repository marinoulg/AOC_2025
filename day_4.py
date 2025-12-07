import pandas as pd

my_input = open("day_4.txt", "r").read()
new = my_input.split("\n")

df = []
for x in range(len(new)-1):
    temp = []
    for i in new[x]:
        temp.append(i)
    df.append(temp)

df = (pd.DataFrame(df))
print(df)

def get_coordinates(df):
    coordinates = []
    for idx in (range(df.shape[0])):
        for col in range(df.shape[1]):
            if df.loc[idx, col] == "@": # for answers
                coordinates.append((idx, col))
    return coordinates

print()
# print(coordinates)

answers_coords_example = [(0, 2),
                          (0, 3),
                          (0, 5),
                          (0, 6),
                          (0, 8),
                          (1, 0),
                          (2, 6),
                          (4, 0),
                          (4, 9),
                          (7, 0),
                          (9, 0),
                          (9, 2),
                          (9, 8)]

# Part 1
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
        # print("count:",count)
        # print('-'*10)

    # print(coords)

    to_be_removed = []
    count = 0
    for key in list(coords.keys()):
        if coords[key] < 4:
            count += 1
            to_be_removed.append(key)
        # print()

    # print()
    # print(count)
    return coords, count, to_be_removed

# coords, count, to_be_removed = remove_forklifts(df)
# print(count)

# print(coords)
# Part 2

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
        break

    print(total)
# print(df)

print(total)



"""
coords = {}
for coordinate in coordinates:
    idx, col = coordinate
    print(f"({idx}, {col})")
    count = 0

    if idx != 0:
        if (idx-1, col) == "@":
            print("option 1: adding 1")
            count += 1
        if (idx-1, col-1) == "@":
            print("option 2: adding 1")
            count += 1
        if (idx-1, col+1) == "@":
            print("option 3: adding 1")
            count += 1

    if col != 0:
        if (idx, col-1) == "@":
            print("option 4: adding 1")
            count += 1

    if idx != df.shape[0]:
        if (idx+1, col) == "@":
            print("option 5: adding 1")
            count += 1
        if (idx+1, col-1) == "@":
            print("option 6: adding 1")
            count += 1
        if (idx+1, col+1) == "@":
            print("option 7: adding 1")
            count += 1

    if col != df.shape[1]:
        if (idx, col+1) == "@":
            print("option 8: adding 1")
            count += 1

    coords[(idx, col)] = count
    print("count:",count)
    print('-'*10)
"""
