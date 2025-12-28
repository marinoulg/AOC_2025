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
    if biggest_x > biggest_y:
        biggest = biggest_x + 1
    else:
        biggest = biggest_y + 1

    for idx in coordinates:
        x,y = idx

    print("coordinates",coordinates)
    print("length of coordinates:", len(coordinates))

    print("first part done")
    return coordinates, biggest_x, biggest_y

def answer_part_1(text_file="example_day_9.txt"):
    coordinates, biggest_x, biggest_y = create_df(text_file)

    big = int()
    length = int(len(coordinates)/2)+1
    for idx in range(length):
        print("iteration n°", idx)
        x_a, y_a = coordinates[idx]
        # print((x_a, y_a))

        for i in range(len(coordinates)):
            x_b, y_b = coordinates[i]

            if x_a != x_b and y_a != y_b:
                # print(f"{(x_a, y_a)} and {(x_b, y_b )}", end=": ")

                longueur = abs((x_a+1)-(x_b+1))+1
                largeur = abs((y_a+1)-(y_b+1))+1
                if big <= largeur*longueur:
                    big = largeur*longueur
                # areas.append(
                #     ((longueur * largeur), \
                #                 (x_a, y_a), (x_b, y_b)))
                # print((longueur, largeur))

        # print()

    print(big)

# answer_part_1()
# print("---"*3)
# answer_part_1("day_9.txt")

# ---------- Part 2 ----------

def get_coordinates(df, to_find="X"):
    coordinates = []
    for idx in (df.index):
        for col in df.columns:
            if df.loc[idx, col] == to_find: # for answers
                coordinates.append((idx, col))
    return coordinates

def create_df_2(text_file="example_day_9.txt"):
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

    return coordinates, biggest_x, biggest_y, df

def get_grid(text_file="example_day_9.txt"):
    coordinates, biggest_x, biggest_y, df = create_df_2(text_file)

    length = len(coordinates)
    for idx in range(length):
        x_a, y_a = coordinates[idx]

        for i in range(len(coordinates)):
            x_b, y_b = coordinates[i]

            if x_a == x_b:
                for x in range(y_a+2, y_b+1):
                    # (y_a+2) bc "+1" so that it matches the new index, and "+1" so that it doesn't overwrite the "#"
                    # (y_b+1) "+1" so that it doesn't overwrite the "#"
                    df.loc[x_b+1,x] = "X"
            elif y_a == y_b:
                for x in range(x_a+2, x_b+1):
                    # (x_a+2) bc "+1" so that it matches the new index, and "+1" so that it doesn't overwrite the "#"
                    # (x_b+1) "+1" so that it doesn't overwrite the "#"
                    df.loc[x, y_a+1] = "X"

    # print(df)

    X_coords = get_coordinates(df)
    for idx in range(length):
        x_a, y_a = X_coords[idx]

        for i in range(len(X_coords)):
            x_b, y_b = X_coords[i]

            if x_a == x_b:
                for x in range(y_a+1, y_b):
                    # print((x_a+1, x))
                    # (y_a+2) bc "+1" so that it matches the new index, and "+1" so that it doesn't overwrite the "#"
                    # (y_b+1) "+1" so that it doesn't overwrite the "#"

                    """
                    si je repasse dessus après je m'en fiche de garder ces conditions là
                    """
                    # if x_a != "#":
                    #     df.loc[x_a,x] = "X"
                    # elif x_b != "#":
                    #     df.loc[x_b,x] = "X"
                    # else:
                    df.loc[x_b+1,x] = "X"

            elif y_a == y_b:
                for x in range(x_a+1, x_b):
                    # (x_a+2) bc "+1" so that it matches the new index, and "+1" so that it doesn't overwrite the "#"
                    # (x_b+1) "+1" so that it doesn't overwrite the "#"
                    """
                    si je repasse dessus après je m'en fiche de garder ces conditions là
                    """
                    # if y_a != "#":
                    #     df.loc[x, y_a] = "X"
                    # elif y_b != "#":
                    #     df.loc[x, y_b] = "X"
                    # else:
                    df.loc[x, y_b] = "X"

    for idx in coordinates:
            x,y = idx
            df.loc[x+1,y+1] = "#"

    return df, coordinates

def answer_part_2(text_file="example_day_9.txt"):
    df, coordinates = get_grid(text_file)

    big = 0
    for idx in range(len(coordinates)):
        print("iteration n°", idx)
        x_a, y_a = coordinates[idx]
        # print((x_a, y_a))

        for i in range(len(coordinates)):
            x_b, y_b = coordinates[i]

            if get_coordinates(df.loc[(min(x_a+1, x_b+1)):max(x_a+1, x_b+1),min(y_a+1, y_b+1):max(y_a+1, y_b+1)], '.') != []:
                # print(f"{(x_a, y_a)} and {(x_b, y_b )} not possible")
                pass

            elif get_coordinates(df.loc[x_a:x_b,y_a:y_b], '.') == []:
                # print(f"{(x_a, y_a)} and {(x_b, y_b )}", end=": ")

                longueur = abs((x_a+1)-(x_b+1))+1
                largeur = abs((y_a+1)-(y_b+1))+1
                if big <= largeur*longueur:
                    big = largeur*longueur

                # print((longueur* largeur))
            else:
                next

    print(big)

print()
print("Part 2")
answer_part_2("day_9.txt")
