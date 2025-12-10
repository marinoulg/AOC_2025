import pandas as pd
import numpy as np

my_input = open("example_day_8.txt", "r").read()
new = my_input.split("\n")

print(new)
# --------------- My functions --------------
X_s = []
Y_s = []
Z_s = []
for elem in new[:-1]:
    x, y, z = (elem.split(','))
    X_s.append(int(x))
    Y_s.append(int(y))
    Z_s.append(int(z))

print(X_s)

print()
def compare_one_with_all(one, X_s, Y_s, Z_s):
    x_compared, y_compared, z_compared = one

    result = int()
    index = int()
    for idx in range(len(X_s)):
        x3 = X_s[idx]
        y3 = Y_s[idx]
        z3 = Z_s[idx]

        temp = np.sqrt((x3-x_compared)**2+(y3-y_compared)**2+(z3-z_compared)**2)
        # print(f"{idx}: {temp}")
        # print()
        if idx == 0:
            result = temp
            index = idx
        elif (temp < result) and (temp != 0):
            result = temp
            index = idx

    print(f"({X_s[index]}, {Y_s[index]}, {Z_s[index]}) and ({X_s[-1]}, {Y_s[-1]}, {Z_s[-1]})")
    return index, result

def know_two_closest(X_s, Y_s, Z_s):
    order = []
    for idx in range(len(X_s)):
        index, result = (compare_one_with_all((X_s[idx], Y_s[idx], Z_s[idx]),
                                    X_s, Y_s, Z_s))
        order.append((result, index, (X_s[idx], Y_s[idx], Z_s[idx])))

    # to be able to easily compare, I create a df
    df = (pd.DataFrame(order).sort_values(by=0).drop(columns=1).rename(columns={0:"distances", 2:"coordinates"}).reset_index())

    # I then find the two closest points
    idx_compared_with_itself = (list(df.iloc[0:1,:]["index"])[0])
    other_idx = (list(df.iloc[1:2,:]["index"])[0])

    # I drop the point in my df that is itself
    # df.drop(index=idx_compared_with_itself, inplace=True)
    return idx_compared_with_itself, other_idx, df

idx_compared_with_itself, other_idx, df = know_two_closest(X_s, Y_s, Z_s)
print(df)
