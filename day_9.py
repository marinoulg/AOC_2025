import pandas as pd
import math

my_input = open("example_day_9.txt", "r").read()
new = my_input.split("\n")

print(new)
# --------------- My functions --------------

def create_df(new):
    coordinates = []
    biggest_x = 0
    biggest_y = 0
    for i in new[:-1]:
        x,y = i.split(",")
        coordinates.append((int(x),int(y)))
        if int(x) >= biggest_x:
            biggest_x = int(x)
        if int(y) >= biggest_y:
            biggest_y = int(y)
    #     temp = []
    #     for i in new[x]:
    #         temp.append(i)
    #     df.append(temp)

    # df = (pd.DataFrame(df))
    # # print(df)
    return coordinates, biggest_x, biggest_y

coordinates, biggest_x, biggest_y = create_df(new)
print(coordinates)
print(biggest_y)
print(biggest_y)
