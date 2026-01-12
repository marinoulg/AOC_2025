import pandas as pd
from time import time
from collections import defaultdict
import numpy as np
import tqdm

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
    biggest_coords = defaultdict(list)
    length = int(len(coordinates)/2)+1

    for idx in range(length):
        x_a, y_a = coordinates[idx]

        for i in range(len(coordinates)):
            x_b, y_b = coordinates[i]

            if x_a != x_b and y_a != y_b:
                longueur = abs((x_a+1)-(x_b+1))+1
                largeur = abs((y_a+1)-(y_b+1))+1
                if big <= largeur*longueur:
                    big = largeur*longueur
                    biggest_coords[big].append([(x_a, y_a), (x_b, y_b)])

    return biggest_coords, max(biggest_coords.keys())

# answer_part_1()
# print("---"*3)
# answer_part_1("day_9.txt")

# ---------- Part 2 ----------

def get_defaultdicts(coordinates, dict_x = defaultdict(set), dict_y = defaultdict(set)):

    copy_dict_x = dict_x.copy()
    copy_dict_y = dict_y.copy()

    for x, y in coordinates:
        copy_dict_x[x].add((y))
        copy_dict_y[y].add((x))

    return copy_dict_x, copy_dict_y

def surround_figure(dict_x, dict_y):
    """
    because we are talking about corners here, it is necessary a set of
    2 coordinates at a time that interest us

    """
    surroundings = []

    for y in tqdm.tqdm(dict_y):
        for i in range(len(dict_y[y])):
            list_tmp = sorted(list(dict_y[y]))

            if len(dict_y[y])%2 == 0:
                if i%2 == 0 and list_tmp[i] != list_tmp[-1]:
                    a,b = (list_tmp)[0+i:2+i]
                    for i in range(a+1,b):
                        surroundings.append((i,y))

            elif len(dict_y[y])%2 == 1:
                    a = (list_tmp)[i]
                    if a != list_tmp[-1]:
                        b = (list_tmp)[i+1]
                        for i in range(a+1,b):
                            surroundings.append((i,y))

    for x in tqdm.tqdm(dict_x):
        for i in range(len(dict_x[x])):
            list_tmp = sorted(list(dict_x[x]))

            if len(dict_x[x])%2 == 0:
                if i%2 == 0:
                    a,b = list_tmp[0+i:2+i]
                    for i in range(a+1,b):
                        surroundings.append((x,i))

            elif len(dict_x[x])%2 == 1:
                    a = (list_tmp)[i]
                    if a != list_tmp[-1]:
                        b = (list_tmp)[i+1]
                        for i in range(a+1,b):
                            surroundings.append((x,i))

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

                        return True
    return False

def filling_in_figure(croix_x, croix_y):
    """
    filled in figure!
    """

    surrs = surround_figure(croix_x, croix_y)
    for elem in tqdm.tqdm(surrs):
        x,y = (elem)
        croix_x[x].add(y)
        croix_y[y].add(x)

    return croix_x, croix_y

def is_possible(coords1, coords2, croix_x, croix_y):
    """
    intermediary function that checks:
        est-ce que mes 4 arrêtes de rectangle sont soit un "#" soit un "x"
    """
    a,b = coords1
    c,d = coords2

    min_b_d = min(b,d)
    max_b_d = max(b,d)
    min_a_c = min(a,c)
    max_a_c = max(a,c)

    # corner_1 = min_a_c,min_b_d
    # corner_2 = min_a_c,max_b_d
    # corner_3 = max_a_c,max_b_d
    # corner_4 = max_a_c,min_b_d

    # 1 ----------- 2 #
    # |             |
    # |             |
    # |             |
    # |             |
    # 4 ----------- 3 #

    # on descend
    for x in tqdm.tqdm(range(min_a_c, max_a_c+1)):
        if x not in croix_y[min_b_d]:
            return False

    for x in tqdm.tqdm(range(min_a_c, max_a_c+1)):
        if x not in croix_y[max_b_d]:
            return False

    # de gauche à droite
    for y in tqdm.tqdm(range(min_b_d, max_b_d+1)):
        if y not in croix_x[min_a_c]:
            return False

    for y in tqdm.tqdm(range(min_b_d, max_b_d+1)):
        if y not in croix_x[max_a_c]:
            return False

    else:
        return True


def part2(text_file="example_day_9.txt"):
    coordinates = create_df(text_file)
    print("step 1 - coordinates created")

    dict_x = defaultdict(set)
    dict_y = defaultdict(set)
    dict_x, dict_y = get_defaultdicts(coordinates,dict_x, dict_y)
    print("step 2 - default dicts dict_x and dict_y created")

    surroundings = surround_figure(dict_x, dict_y)
    print("step 3 - surroundings created")

    croix_x, croix_y = get_defaultdicts(surroundings, dict_x, dict_y)
    print("step 4 - default dicts croix_x and croix_y created, filling in figure now")

    croix_x, croix_y = filling_in_figure(croix_x, croix_y)
    print("step 5 - figure has been filled in")

    big = 0
    biggest_coords = defaultdict(list)

    for idx in tqdm.tqdm(range(len(coordinates))):
        a,b = coordinates[idx]

        for i in range(len(coordinates)):
            c,d = coordinates[i]

            min_b_d = min(b,d)
            max_b_d = max(b,d)
            min_a_c = min(a,c)

            corner_1 = min_a_c,min_b_d
            corner_2 = min_a_c,max_b_d

            # ZERO PHASE : est-ce que j'ai bien un rectangle, et pas une ligne ou un point
            if a != b and c != d and (a,b) != (c,d) and a != c and b != d:

                #  FIRST PHASE : est-ce que mes 4 coins de rectangle sont soit un "#" soit un "x"
                if all_corners_possible(corner_1, corner_2, dict_x, dict_y, croix_x, croix_y):

                    # SECOND PHASE : vérifier que mon rectangle est malgré tout possible`
                    if is_possible((a,b), (c,d), croix_x, croix_y):
                        # THIRD PHASE : calculer l'aire de mon rectangle
                        longueur = abs((a+1)-(c+1))+1
                        largeur = abs((b+1)-(d+1))+1
                        if big <= largeur*longueur:
                            big = largeur*longueur
                            biggest_coords[big].append([(a, b), (c, d)])

    return max(biggest_coords)


if __name__ == "__main__":
    part2("day_9.txt")
