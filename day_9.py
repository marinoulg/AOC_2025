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
                #  si oui, rectangle *impossible* --> pas toujours : contre-exemple (1,7) et (5,9)
                    # for elem in range(b+1,d-1):
                    #     if elem in dict_x[a]:
                    #         break
                    # else:
                    #     for elem in range(b+1,d-1):
                    #         if elem in dict_x[c]:
                    #             break
                    #     else:
                    #         for elem in range(a+1,c-1):
                    #             if elem in dict_y[d]:
                    #                 break
                    #         else:
                    #             for elem in range(a+1,c-1):
                    #                 if elem in dict_y[b]:
                    #                     break
                    #             else:
                    #                 print('ok possible rectangle')

    # Rq : partir des biggest rectangles identified in part 1 ?

    """
    cette partie là ne fonctionne pas encore
    """
    big = 0
    biggest_coords = defaultdict(list)

    for idx in range(len(coordinates)):
        a,b = coordinates[idx]

        for i in range(len(coordinates)):
            c,d = coordinates[i]

            corner_1 = a,b
            corner_2 = c,d

            # ZERO PHASE : est-ce que j'ai bien un rectangle, et pas une ligne ou un point
            if a != b and c != d and (a,b) != (c,d) and a != c and b != d:

                #  FIRST PHASE : est-ce que mes 4 coins de rectangle sont soit un "#" soit un "x"
                if all_corners_possible(corner_1, corner_2, dict_x, dict_y, croix_x, croix_y):

                    # SECOND PHASE : vérifier que mon rectangle est malgré tout possible
                    """
                    WIP
                    """

                    # THIRD PHASE : calculer l'aire de mon rectangle
                    longueur = abs((a+1)-(c+1))+1
                    largeur = abs((b+1)-(d+1))+1
                    if big <= largeur*longueur:
                        big = largeur*longueur
                        biggest_coords[big].append([(a, b), (c, d)])

    return biggest_coords
