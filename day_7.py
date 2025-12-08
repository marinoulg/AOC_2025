import pandas as pd
import math

my_input = open("example_day_7.txt", "r").read()
new = my_input.split("\n")

# print(new)

df = []
for x in range(len(new)-1):
    temp = []
    for i in new[x]:
        temp.append(i)
    df.append(temp)

df = (pd.DataFrame(df))
print(df)

def get_coordinates(df, to_find="@"):
    coordinates = []
    for idx in (range(df.shape[0])):
        for col in range(df.shape[1]):
            if df.loc[idx, col] == to_find: # for answers
                coordinates.append((idx, col))
    return coordinates

print()
coordinates = get_coordinates(df, "^")
print(coordinates)

print()
S = get_coordinates(df, "S")[0]

# print()

def when_encounter_truc(S, df):
    """
    S: 1 set of coordinates
    Ex: S = (x, y) or S = (idx, col)
    """
    # new_S = [(S[0]+2, S[1]-1),
    #          (S[0]+2, S[1]+1)]

    # count = 0

    if df.loc[S] == "^":
        df.loc[S[0], S[1]+1] = "|"
        # count += 1
    else:
        print(False)

    if df.loc[S] == "^":
        # print(S[0], S[0]-1)
        df.loc[S[0], S[1]-1] = "|"
    else:
        pass

    return df #, count #, new_S

# def when_encounter_truc_left(S, df):
#     print(S)

# count = 0
for i in range(len(coordinates)):
    A = (coordinates[i])
    df = when_encounter_truc(A, df)
    # count += c
    # df=when_encounter_truc_right(A, df)

# print(df.loc[A], A)
# print(df.loc[A[0]+1, A[1]+1], (A[0]+1, A[1]+1))
# print(df.loc[A[0]+1, A[0]-1], (A[0]+1, A[1]-1))

print(df)
# print()
# print(count)
# print(ns)

trait_droit = get_coordinates(df, "|")

trait = trait_droit[0]


def go_straight(trait, df, sign="|"):
    """
    Also to be considered at the start.

    'trait' is one tuple of coordinates for a trait.
    Ex: trait = (idx, col)

    trait = trait_droit[0]
    trait_droit = get_coordinates(df, "|")
    """

    # print(df.loc[3,6])
    # print("before condition:", (trait[0]+1, trait[1]))
    if df.loc[(trait[0]+1, trait[1])] != "^": #"== "." :
        # print("trait:", (trait[0]+1, trait[1]))
        print((trait[0]+1, trait[1]))
        df.loc[(trait[0]+1, trait[1])] = sign
    else:
        # print("no")
        return df

    # print(df)
    return df

for i in range(len(trait_droit)):
    df = go_straight(trait_droit[i], df)

print(df)

print("we are here")

trait_droit = get_coordinates(df, "|")

max_lines = df.shape[0]-1

for i in range(len(trait_droit)):
    if (trait_droit[i][0] != max_lines): # or (coord[1] != df.shape[1]):
        # c+=1
        df = go_straight(trait_droit[i], df, "|")
        # print(True)
    else:
        print(False)

trait_droit = get_coordinates(df, "|")

max_lines = df.shape[0]-1

for i in range(len(trait_droit)):
    if (trait_droit[i][0] != max_lines): # or (coord[1] != df.shape[1]):
        # c+=1
        df = go_straight(trait_droit[i], df, "|")
        # print(True)
    else:
        print(False)

print(df)
