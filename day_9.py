import pandas as pd
import math

def create_df(text_file="example_day_9.txt"):
    my_input = open(text_file, "r").read()
    new = my_input.split("\n")

    coordinates = []
    biggest_x = 0
    biggest_y = 0
    for i in new[:-1]:
        x,y = i.split(",")
        coordinates.append((int(y),int(x)))

    biggest_x = pd.DataFrame(coordinates).sort_values(by=0, ascending=False).reset_index().loc[0,0]
    biggest_y = pd.DataFrame(coordinates).sort_values(by=0, ascending=False).reset_index().loc[0,1]

    return coordinates, biggest_x, biggest_y

def answer_part_1(text_file="example_day_9.txt"):
    coordinates, biggest_x, biggest_y = create_df(text_file)
    if biggest_x > biggest_y:
        biggest = biggest_x + 1
    else:
        biggest = biggest_y + 1

    df = pd.DataFrame([['.']*(biggest_y+2)]*(biggest+1)).T

    for idx in coordinates:
        x,y = idx
        df.loc[x,y] = "#"

    df.index = list(range(1,df.shape[0]+1))
    df.columns = list(range(1,df.shape[1]+1))
    print("shape:",df.shape)
    print("coordinates",coordinates)
    print("length of coordinates:", len(coordinates))

    """
    seconde partie de l'exercice
    --> ça bloque ici car pas assez de RAM
    """
    big = int()
    length = int(len(coordinates)/2)+1
    for idx in range(length):
        x_a, y_a = coordinates[idx]
        print((x_a, y_a))

        for i in range(len(coordinates)):
            x_b, y_b = coordinates[i]

            if x_a != x_b and y_a != y_b:
                print(f"{(x_a, y_a)} and {(x_b, y_b )}", end=": ")

                longueur = abs((x_a+1)-(x_b+1))+1
                largeur = abs((y_a+1)-(y_b+1))+1
                if big <= largeur*longueur:
                    big = largeur*longueur
                # areas.append(
                #     ((longueur * largeur), \
                #                 (x_a, y_a), (x_b, y_b)))
                print((longueur, largeur))
        print()

    print(big)

answer_part_1()
print("---"*3)
answer_part_1("day_9.txt")
