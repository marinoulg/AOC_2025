import pandas as pd
import math

my_input = open("example_day_6.txt", "r").read()
new = my_input.split("\n")

coordinates_spaces = []
for idx in range(len(new)):
    for col in range(len(new[idx])):
        if new[idx][col] == " ":
            coordinates_spaces.append((idx, col))

print('step 1 done')

useless_coord = []
for coord in coordinates_spaces:
    idx, col = coord
    # for i in range(len(coordinates_spaces)):-idx):
    # while (idx+1) < (len(coordinates_spaces)):
    if ((idx+1), col) not in coordinates_spaces:
                useless_coord.append((idx, col))
                idx = idx+1

print('step 2 done')

good_coordinates = coordinates_spaces.copy()
for useless in useless_coord:
    if useless in good_coordinates:
        good_coordinates.remove(useless)

# print(good_coordinates)

nb_lines = []
nb_col = []
for coord in good_coordinates:
    idx, col = coord
    nb_lines.append(idx)
    nb_col.append(col)

print('step 3 done')
# print() # "nb lines", max(nb_lines)

by_line = []
for x in range(max(nb_col)):
    temp = []
    for coord in good_coordinates:
        idx, col = coord
        if idx == x:
            temp.append(coord)
    if temp != []:
        by_line.append(temp)

# print(good_coordinates)
# print("before by line")
# print(by_line)

# print("nb col", (nb_col))

print('step 4 done')

to_keep = []
for coord in by_line[0]:
    idx, col = coord
    # print(coord)
    for i in range(max(nb_col)):
        # print(tuple((idx+i, col)))

        if tuple((idx+i, col)) in good_coordinates:
            to_keep.append((idx+i, col))

print("to keep:", to_keep)
nb_of_lines = (len(new)-2)
nb_of_columns = (len(to_keep)//nb_of_lines) + 1

total = []
for _ in range(nb_of_columns): # bc 4 spaces to delimitate
    column = []
    for i in range(nb_of_lines): # bc 3 lines
        idx, col = to_keep[0]
        print(int(new[i][idx:col].strip()))
        column.append(int(new[i][idx:col].strip()))
        # print(new[i][idx:col])
        new[i] = new[i].replace(new[i][idx:col+1], "")
    total.append(column)

signs = []
for char in (new[-2]):
    if char =="+" or char == "*":
        signs.append(char)

df = pd.DataFrame(total).T
# print(df)

df_signs = pd.DataFrame(signs).T
df_signs.rename(index={0:df.shape[0]+1}, inplace=True)

df = (pd.concat([df, df_signs]))
# print(df.shape[0])
df.reset_index(drop="index", inplace=True)

# print(df)

final_result = []
for col in range(df.shape[1]):
    if df.loc[df.shape[0]-1, col] == "*":
        final_result.append(math.prod(df.loc[0:df.shape[0]-2,col]))
    elif df.loc[df.shape[0]-1, col] == "+":
        final_result.append(sum(df.loc[0:df.shape[0]-2,col]))

print(sum(final_result))
