import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# --------------- Part 1 --------------

def create_df(input_file = "example_day_7.txt"):
    my_input = open(input_file, "r").read()
    new = my_input.split("\n")

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

def get_part_1(input_file="example_day_7.txt"):

    df = create_df(input_file)

    S = get_coordinates(df, "S")[0]
    df = go_straight(S, df)

    coordinates = get_coordinates(df, "^")

    df = surround_truc_with_traits(df, coordinates)
    df, trait_droit = get_all_traits(df)


    count = 0
    for i in range(len(coordinates)):
        c = get_surrounding_coordinates_truc(coordinates[i], df)
        count += (c)

    # print(count)
    return df



# --------------- Part 2 --------------

def is_un_trait(idx, col, df):
    return df.loc[(idx, col)] == "|"

def is_truc(idx, col, df):
    if df.loc[idx, col] == "^":
        return True


def connections(df, coords):
    my_dict = dict()

    try:
        for coord in coords:
            idx, col = coord
            temp = []

            if df.loc[idx+2, col-1] == "^":
                temp.append((idx+2, col-1))
            else:
                for i in range(idx+1, (df.shape[0])):
                        if is_truc(i, col-1, df) == True:
                            temp.append((i, col-1))
                            # break

                        # elif is_truc(i, col-2, df) == True:
                        #     temp.append((i, col-2))
                        # break


            if df.loc[idx+2, col+1] == "^":
                temp.append((idx+2, col+1))
            else:
                for i in range(idx+1, (df.shape[0])):
                    if is_truc(i, col+1, df) == True:
                        temp.append((i, col+1))
                        # break

                    # elif is_truc(i, col+2, df) == True:
                    #     temp.append((i, col+2))
                        # break

            # print(temp)
            my_dict[(idx, col)] =  temp

    except KeyError:
        next

    return my_dict

def draw_graph(df):
    coords = get_coordinates(df, "^")
    G = nx.DiGraph()
    my_dict = connections(df, coords)

    for key, value in my_dict.items():
        if isinstance(value, list):
            for i in range(len(value)):
                G.add_edge(key, value[i])
        else:
            G.add_edge(key, value[i])

    """for col in range(df.shape[1]):
        if is_truc(df.shape[0]-2,col):
            truc = (df.shape[0]-2,col)

            if df.loc[df.shape[0]-1,col] == "|" :
                G.add_edge(truc, (df.shape[0]-1,col))"""

    return my_dict, G

def get_start_and_ends(coords, df):
    start = coords[0]
    ends = []

    for col in range(df.shape[1]):
        if df.loc[df.shape[0]-1,col] == "|" :
            ends.append((df.shape[0]-1,col))

    # for i in range(len(coords)):
    #     if coords[i][0] == end_idx:
    #         ends.append(coords[i])

    # nx.draw(G, with_labels=True)
    # plt.show()

    return start, ends

def get_paths(start, ends, G):
    paths = []
    for i in range(len(ends)):
        print(ends[i], end=": ")
        print(len((list(nx.all_simple_paths(G, start, ends[i])))))
        paths.append(len((list(nx.all_simple_paths(G, start, ends[i])))))
        # if (len((list(nx.all_simple_paths(G, start, ends[i]))))) == 1:
        #     print(((list(nx.all_simple_paths(G, start, ends[i])))))

    return sum(paths)

def get_part_2(input_file="example_day_7.txt"):

    # df = create_df(input_file)
    df = get_part_1(input_file)
    coords = get_coordinates(df, "^")
    start, ends = get_start_and_ends(coords, df)
    ends_final = []
    for coord in ends:
        df.loc[coord[0]+1, coord[1]] = "^"
        ends_final.append((coord[0]+1, coord[1]))

    my_dict, G = draw_graph(df)
    for col in range(df.shape[1]):
            if is_truc(df.shape[0]-2,col,df):
                truc = (df.shape[0]-2,col)

                if df.loc[df.shape[0]-1,col] == "|" :
                    G.add_edge(truc, (df.shape[0]-1,col))

    paths = get_paths(start, ends_final, G)
    return paths

if __name__ == "__main__":
    # get_part_1()
    # print("---"*3)
    # get_part_1("day_7.txt")

    res = get_part_2()
    print(res)
