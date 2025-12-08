import pandas as pd
import math

my_input = open("example_day_7.txt", "r").read()
new = my_input.split("\n")

# print(new)
# --------------- My functions --------------

def create_df(new):
    df = []
    for x in range(len(new)-1):
        temp = []
        for i in new[x]:
            temp.append(i)
        df.append(temp)

    df = (pd.DataFrame(df))
    # print(df)
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
        # count += 1
    else:
        print(False)

    if df.loc[S] == "^":
        # print(S[0], S[0]-1)
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

    # print(df.loc[3,6])
    # print("before condition:", (trait[0]+1, trait[1]))
    if df.loc[(trait[0]+1, trait[1])] != "^": #"== "." :
        # print("trait:", (trait[0]+1, trait[1]))
        # print((trait[0]+1, trait[1]))
        df.loc[(trait[0]+1, trait[1])] = sign
    else:
        # print("no")
        return df

    # print(df)
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
                # c+=1
                df = go_straight(trait_droit[i], df, "|")
                # print(True)
            # else:
                # print(False)

        trait_droit = get_coordinates(df, "|")
        if len(trait_droit) == temp:
            print(f"break at {_} iterations")
            break
    # print(df)
    return df


# --------------- My code --------------


df = create_df(new)

S = get_coordinates(df, "S")[0]
df = go_straight(S, df)

coordinates = get_coordinates(df, "^")

df = surround_truc_with_traits(df, coordinates)
df = get_all_traits(df)

print(df)
