import pandas as pd
from time import time
from collections import defaultdict

def create_df(text_file="example_day_9.txt"):
    my_input = open(text_file, "r").read()
    new = my_input.split("\n")

    coordinates = []
    for i in new[:-1]:
        x,y = i.split(",")
        coordinates.append((int(y),int(x)))

    print("length of coordinates:", len(coordinates))

    print("first part done")
    return coordinates

def answer_part_1(text_file="example_day_9.txt"):
    coordinates = create_df(text_file)

    big = int()
    length = int(len(coordinates)/2)+1
    for idx in range(length):
        # print("iteration n°", idx)
        x_a, y_a = coordinates[idx]

        for i in range(len(coordinates)):
            x_b, y_b = coordinates[i]

            if x_a != x_b and y_a != y_b:
                longueur = abs((x_a+1)-(x_b+1))+1
                largeur = abs((y_a+1)-(y_b+1))+1
                if big <= largeur*longueur:
                    big = largeur*longueur

    # print(big)

# answer_part_1()
# print("---"*3)
# answer_part_1("day_9.txt")

# ---------- Part 2 ----------

def get_defaultdicts(coordinates):

    dict_x = defaultdict(set)
    dict_y = defaultdict(set)

    for x, y in coordinates:
        # print(x,y)
        dict_x[x].add((y))
        dict_y[y].add((x))

    return dict_x, dict_y

def surround_figure(dict_x, dict_y):
    """
    because we are talking about corners here, it is necessary a set of
    2 coordinates at a time that interest us

    need to find a way to not just surround the figure but fill it in,
    taking into account that the total of "x"s are not necessarily %2 == 0
    """
    surroundings = []

    for y in dict_y:
        for i in range(len(dict_y[y])):
            if i%2 == 0:
                a,b = sorted(list(dict_y[y]))[0+i:2+i]
                for i in range(a+1,b):
                    surroundings.append((i,y))
                    # df.loc[(i,y)] = "x"
            elif i%2 != 0 and i == len(dict_y[y]):
                """
                WIP: might be something like this
                """
                pass

    for x in dict_x:
        for i in range(len(dict_x[x])):
            if i%2 == 0:
                a,b = sorted(list(dict_x[x]))[0+i:2+i]
                for i in range(a+1,b):
                    surroundings.append((x,i))
                    # df.loc[(x, i)] = "x"


    return surroundings

def all_corners_possible(corner_1, corner_2, dict_x, dict_y, croix_x, croix_y):
    """
    intermediary function that checks:
        est-ce que mes 4 coins de rectangle sont soit un "#" soit un "x"
    """
    a,b = corner_1
    c,d = corner_2

    if b in dict_x[a] or b in croix_x[a]:
        if d in dict_x[a] or d in croix_x[a]:

            if a in dict_y[b] or a in croix_y[b]:
                if c in dict_y[b] or c in croix_y[b]:
                        # print(corner_1, corner_2)
                        return True

def part2_WIP(text_file="example_day_9.txt"):
    coordinates = create_df(text_file)
    dict_x, dict_y = get_defaultdicts(coordinates)
    surroundings = surround_figure(dict_x, dict_y)
    croix_x, croix_y = get_defaultdicts(surroundings)

    #  si je teste deux paires de coordonnées :
        #  est-ce que mes 4 coins de rectangle sont soit un "#" soit un "x"
            #  si oui, est-ce que j'ai au moins un autre "#" dans le périmètre de mon rectangle ?
            #  si non, rectangle possible
                #  si oui, rectangle impossible --> pas toujours : contre-exemple (1,7) et (5,9)

    # Rq : partir des biggest rectangles identified in part 1 ?

    """
    cette partie là ne fonctionne pas encore
    """

    for idx in range(len(coordinates)):
        a,b = coordinates[idx]

        for i in range(len(coordinates)):
            c,d = coordinates[i]

            corner_1 = a,b
            corner_2 = c,d

            # corner_3 = (a,d)
            # corner_4 = (b,c)

            first_phase = []

            #  FIRST PHASE : est-ce que mes 4 coins de rectangle sont soit un "#" soit un "x"
            if all_corners_possible(corner_1, corner_2, dict_x, dict_y, croix_x, croix_y):
                pass


"""
def to_visualise(text_file = "example_day_9.txt"):

    coordinates = create_df(text_file)
    new_coords = get_all_suroundings(coordinates)

    big_x = 0
    big_y = 0
    for elem in new_coords:
        if big_x < elem[0]:
            big_x = elem[0]
        if big_y < elem[1]:
            big_y = elem[1]

    df= pd.DataFrame([["."]*(big_y+1)]*(big_x+1))

    for elem in new_coords:
        df.loc[elem] = "x"

    nc = get_all_suroundings(new_coords)
    for elem in nc:
        df.loc[elem] = "x"

    for elem in coordinates:
        df.loc[elem] = "#"

    return df

def get_all_suroundings(coordinates):

    new_coords = coordinates.copy()

    big = int()
    length = (len(coordinates))
    for idx in range(length):
        x_a, y_a = coordinates[idx]

        for i in range(len(coordinates)):
            x_b, y_b = coordinates[i]

            if x_a == x_b:
                # print(f"{(x_a, y_a)} and {(x_b, y_b)}:", end="")
                mini = min(y_a, y_b)
                maxi = max(y_a, y_b)

                for i in range(mini+1, maxi):
                    if (x_a, i) not in new_coords:
                        # print((x_a, i), end=",")
                        new_coords.append((x_a, i))
                # print()

            elif y_a == y_b:
                # print(f"{(x_a, y_a)} and {(x_b, y_b)}:", end="")
                mini = min(x_a, x_b)
                maxi = max(x_a, x_b)

                for i in range(mini+1, maxi):
                    if (i, y_a) not in new_coords:
                        # print((i, y_a), end=",")
                        new_coords.append((i, y_a))
    print(f"surroundings gathered for {len(coordinates)}")
    return new_coords


def check_if_a_pair_is_possible(pair1, pair2, nc):

    xa, ya = pair1
    xb, yb = pair2

    mini_x = min(xa,xb)
    maxi_x = max(xa,xb)

    mini_y = min(ya,yb)
    maxi_y = max(ya,yb)

    for y_change in range(mini_y, maxi_x+1):
        for x_change in range(mini_x, maxi_x+1):
            if ((x_change, y_change)) not in nc:
                # print(f"{(xa, xb)} and {(ya, yb)} not possible")
                return 0

    else:
        # print(f"{(xa, xb)} and {(ya, yb)} possible")
        return (maxi_x+1-mini_x)*(maxi_y+1-mini_y) # area of pair1 and pair2

def answer_part_2(text_file="example_day_9.txt"):
    coordinates = create_df(text_file)
    new_coords = get_all_suroundings(coordinates)
    nc = get_all_suroundings(new_coords)
    biggest_area = 0

    for idx_pair1 in range(len(coordinates)):
        pair1 = nc[idx_pair1]
        for idx_pair2 in range(len(coordinates)):
            pair2 = nc[idx_pair2]

            # print("pair1:", pair1, end=" and ")
            # print("pair2:", pair2)

            if pair1 != pair2:
                checking = check_if_a_pair_is_possible(pair1=pair1, pair2=pair2, nc=nc)

                if checking > biggest_area:
                        # print(checking)
                        biggest_area = checking
    return biggest_area

now = (time())
print(answer_part_2("day_9.txt"))
end = time()
print(end-now)
"""
