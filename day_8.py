import pandas as pd
import numpy as np

my_input = open("example_day_8.txt", "r").read()
new = my_input.split("\n")

# print(new)
# --------------- My functions --------------
def create_lists_for_x_y_z(new):
    X_s = []
    Y_s = []
    Z_s = []
    for elem in new[:-1]:
        x, y, z = (elem.split(','))
        X_s.append(int(x))
        Y_s.append(int(y))
        Z_s.append(int(z))
    return X_s, Y_s, Z_s


def compare_one_with_all(one_idx):
    X_s, Y_s, Z_s = create_lists_for_x_y_z(new)
    x_compared, y_compared, z_compared = X_s[one_idx], Y_s[one_idx], Z_s[one_idx]

    results = []
    indexes = []

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
        results.append(temp)
        indexes.append(idx)

    # print(f"({X_s[index]}, {Y_s[index]}, {Z_s[index]}) and ({X_s[-1]}, {Y_s[-1]}, {Z_s[-1]})")
    return index, result, results, indexes

def know_two_closest(X_s, Y_s, Z_s, is_not=None):
    order = []
    for idx in range(len(X_s)):
        index, result = (compare_one_with_all((X_s[idx], Y_s[idx], Z_s[idx]),
                                    X_s, Y_s, Z_s))
        order.append((result, index, (X_s[idx], Y_s[idx], Z_s[idx])))

    # to be able to easily compare, I create a df
    df = (pd.DataFrame(order).sort_values(by=0).drop(columns=1).rename(columns={0:"distances", 2:"coordinates"}).reset_index())

    if is_not != None:
        to_drop = []
        for elem in is_not:
            idx_to_be_dropped = list(df[df["distances"]==elem].index)[0]
            to_drop.append(idx_to_be_dropped)
        df.drop(index=to_drop, inplace=True)
        df.reset_index(inplace=True)

    idx_compared_with_itself = (list(df.iloc[0:1,:]["index"])[0])
    other_idx = (list(df.iloc[1:2,:]["index"])[0])
    res = df.loc[1,"distances"]

    # I drop the point in my df that is itself
    # df.drop(index=idx_compared_with_itself, inplace=True)
    return idx_compared_with_itself, other_idx, df, res


index_ = []
compared_with_index = []
result_ = []
all_results = []
X_s, Y_s, Z_s = create_lists_for_x_y_z(new)
for idx in range(len(X_s)):
    # print(idx)
    index, result, results, indexes = (compare_one_with_all(idx))
    # order.append((results, indexes, (X_s[idx], Y_s[idx], Z_s[idx])))
    print("index:", index)
    index_.append(index)
    print("compared with index:",idx)
    compared_with_index.append(idx)
    print("result:", result)
    result_.append(result)
    print("results:", results)
    all_results.append(results)
    # print("all indexes:", indexes)
    print()

df = pd.DataFrame([index_, compared_with_index, result_, all_results])
print()
print(df)


# idx_compared_with_itself, other_idx, df, res = know_two_closest(X_s, Y_s, Z_s)

# to_drop = list()
# for _ in range(df.shape[0]):
#     idx_compared_with_itself, other_idx, df, res = know_two_closest(X_s, Y_s, Z_s, is_not=to_drop)
#     print(idx_compared_with_itself, other_idx)
#     to_drop.append(res)

# idx_compared_with_itself, other_idx, df, res = know_two_closest(X_s, Y_s, Z_s, is_not=to_drop)
# print(idx_compared_with_itself, other_idx)
# to_drop.append(res)

# idx_compared_with_itself, other_idx, df, res = know_two_closest(X_s, Y_s, Z_s, is_not=to_drop)
# print(idx_compared_with_itself, other_idx)
# to_drop.append(res)

# idx_compared_with_itself, other_idx, df, res = know_two_closest(X_s, Y_s, Z_s, is_not=to_drop)
# print(idx_compared_with_itself, other_idx)
# to_drop.append(res)

# idx_compared_with_itself, other_idx, df, res = know_two_closest(X_s, Y_s, Z_s, is_not=to_drop)
# print(idx_compared_with_itself, other_idx)
# to_drop.append(res)

# idx_compared_with_itself, other_idx, df, res = know_two_closest(X_s, Y_s, Z_s, is_not=to_drop)
# print(idx_compared_with_itself, other_idx)
# to_drop.append(res)
