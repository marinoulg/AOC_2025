import pandas as pd
import math

my_input = open("example_day_7.txt", "r").read()
new = my_input.split("\n")

# --------------- My functions --------------

def create_df(new):
    df = []
    for x in range(len(new)-1):
        temp = []
        for i in new[x]:
            temp.append(i)
        df.append(temp)

    df = (pd.DataFrame(df))
    return df

def get_coordinates(df, to_find="@"):
    coordinates = []
    for idx in (range(df.shape[0])):
        for col in range(df.shape[1]):
            if df.loc[idx, col] == to_find: # for answers
                coordinates.append((idx, col))
    return coordinates

def when_encounter_truc(S, df):
    """
    S: 1 set of coordinates
    Ex: S = (x, y) or S = (idx, col)
    """

    if df.loc[S] == "^":
        df.loc[S[0], S[1]+1] = "|"
    else:
        print(False)

    if df.loc[S] == "^":
        df.loc[S[0], S[1]-1] = "|"
    else:
        pass

    return df

def surround_truc_with_traits(df, coordinates):
    for i in range(len(coordinates)):
        A = (coordinates[i])
        df = when_encounter_truc(A, df)
    return df

def go_straight(trait, df, sign="|"):
    """
    Also to be considered at the start.

    'trait' is one tuple of coordinates for a trait.
    Ex: trait = (idx, col)

    trait = trait_droit[0]
    trait_droit = get_coordinates(df, "|")
    """

    if df.loc[(trait[0]+1, trait[1])] != "^": #"== "." :
        df.loc[(trait[0]+1, trait[1])] = sign
    else:
        return df

    return df

def get_all_traits(df):
    """
    Looping '_' iterations in order to create the traits
    if at (idx+1, col) != "^"
    so that we create all the lines of the puzzle.
    """

    trait_droit = get_coordinates(df, "|")
    max_lines = df.shape[0]-1

    for _ in range(10):
        temp = len(trait_droit)
        for i in range(len(trait_droit)):
            if (trait_droit[i][0] != max_lines): # or (coord[1] != df.shape[1]):
                df = go_straight(trait_droit[i], df, "|")

        trait_droit = get_coordinates(df, "|")
        if len(trait_droit) == temp:
            # print(f"break at {_} iterations")
            break

    return df, trait_droit

def get_surrounding_coordinates_truc(coord, df):
    """
    A truc is splitted if:
        - above truc: | (un trait)
        - left of truc: | (un trait)
        - right of truc: | (un trait)

    coord = coordinates[0],
    coord = (idx, col) --> 1 set of coordinates for 1 truc "^"
    """
    idx, col = coord

    count = 0
    if (df.loc[(idx-1, col)] == "|"): # above truc: | (un trait)
        if (df.loc[(idx, col+1)] == "|"): # right of truc: | (un trait)
            if (df.loc[(idx, col-1)] == "|"): # left of truc: | (un trait)
                count+= 1
    return count

# --------------- My code --------------

# Part 1
def get_part_1(day_7="example_day_7.txt"):
    my_input = open(day_7, "r").read()
    new = my_input.split("\n")

    df = create_df(new)

    S = get_coordinates(df, "S")[0]
    df = go_straight(S, df)

    coordinates = get_coordinates(df, "^")

    df = surround_truc_with_traits(df, coordinates)
    df, trait_droit = get_all_traits(df)


    count = 0
    for i in range(len(coordinates)):
        c = get_surrounding_coordinates_truc(coordinates[i], df)
        count += (c)

    print(count)

get_part_1()
print("---"*3)
get_part_1("day_7.txt")

# Part 2

# ordre de grandeur between (6**2) and (7**2)
# 6 : car 6 splitters in reality in example, if not consider that we always go left at the first one
# et que we have 1 chance sur 2 d'aller à gauche ou bien à droite, hence "to the power of 2"

# formule statistique probable existe, à trouver
# lien possible avec les decisions trees

df = create_df(new)
# get_coordinates(df)
# print(df)
