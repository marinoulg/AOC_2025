import pandas as pd

def get_ranges(text_file="example_day_5.txt"):
    """
    get the ranges in the text_file
    """
    my_input = open(text_file, "r").read()
    new = my_input.split("\n")

    list_1=list()
    list_2 = list()
    for i in range(len((new))):
        if new[i] != '':
            list_1.append(new[i])
        else:
            for idx in range(i+1, len((new))-1):
                list_2.append(new[idx])
            break

    ranges_ = []
    for idx in range(len(list_1)):
        a, b = list_1[idx].split("-")
        ranges_.append([int(a), int(b)])

    return ranges_, list_2

def part_1(text_file="example_day_5.txt"):
    """
    Count the number of ingredients that are spoiled, aka NOT fresh.
    """
    ranges_, list_2 = get_ranges(text_file)
    count = 0
    for num in list_2:
        count_tmp = 0
        for ranges in ranges_:
            if int(num) < ranges[0] or int(num) > ranges[1]:
                count_tmp += 1
        if count_tmp == len(ranges_):
            count += 1

    print("total count of FRESH is: ", (len(list_2))-count)
    return len(list_2)-count

print(part_1("day_5.txt"))

# ---------------- Part 2 ----------------

# (part_1())

# df = pd.DataFrame(ranges_)
# df = df.sort_values(by=0)
# df.drop_duplicates(inplace=True)
# print(df)
print()

# print(df.shape)
# print()

def reset_ranges(df):
    idx_to_be_dropped = []
    df.reset_index(drop="index", inplace=True)
    for i in range((df.shape[0])-2):
        if (df.loc[i, 0] <  df.loc[i+1, 0] <  df.loc[i, 1]):
            print("index to be dropped is ", (i+1))
            print(f"{df.loc[i, 1]} is to be replaced by {df.loc[i+1, 1]}")
            df.loc[i, 1] = df.loc[i+1, 1]
            idx_to_be_dropped.append((i+1))
            # df = df.drop(index=i+1)
            # df.reset_index(drop="index", inplace=True)
            # print(df)

    return df, idx_to_be_dropped

df, idx_to_be_dropped = reset_ranges(df)
# print(df.shape)
# print(idx_to_be_dropped)
# print(df)

for idx in idx_to_be_dropped:
    print(idx)
    df.drop(index=idx, inplace=True)

print()
print("total number of indexes dropped: ", len(idx_to_be_dropped))
# print()
# print(df)
df.reset_index(drop="index", inplace=True)

# df.reset_index(drop="index", inplace=True)
# if (df.loc[(df.shape[0])-2, 0] <  df.loc[(df.shape[0])-1, 0] <  df.loc[(df.shape[0])-2, 1]):
#         # print("index to be dropped is ", -1)
#         # print(f"{df.loc[(df.shape[0])-2, 1]} is to be replaced by {df.loc[(df.shape[0])-1, 1]}")
#         df.loc[(df.shape[0])-2, 1] = df.loc[(df.shape[0])-1, 1]

#         df = df.drop(index=(df.shape[0])-1)
#         # idx_to_be_dropped.append((df.shape[0])-1)
#         df.reset_index(drop="index", inplace=True)


def get_all_ranges_overlapping(df):
    for _ in range(df.shape[0]):
        # df = reset_ranges(df)

        df, idx_to_be_dropped = reset_ranges(df)
        # print(df.shape)
        # print(idx_to_be_dropped)
        # print(df)

        for idx in idx_to_be_dropped:
            print(idx)
            df.drop(index=idx, inplace=True)



        # print()
        # print("total number of indexes dropped: ", len(idx_to_be_dropped))

        # print(df)
        df.reset_index(drop="index", inplace=True)

        df.reset_index(drop="index", inplace=True)
        if (df.loc[(df.shape[0])-2, 0] <  df.loc[(df.shape[0])-1, 0] <  df.loc[(df.shape[0])-2, 1]):
                # print("index to be dropped is ", -1)
                # print(f"{df.loc[(df.shape[0])-2, 1]} is to be replaced by {df.loc[(df.shape[0])-1, 1]}")
                df.loc[(df.shape[0])-2, 1] = df.loc[(df.shape[0])-1, 1]

                df = df.drop(index=(df.shape[0])-1)
                # idx_to_be_dropped.append((df.shape[0])-1)
                df.reset_index(drop="index", inplace=True)
    print(df.shape)
    return df

print(df)
for _ in range(df.shape[0]):
    print("iteration n°", _)
    df = get_all_ranges_overlapping(df)
    df.sort_values(by=0, inplace=True)
print(df)

df.drop_duplicates(inplace=True)
df.reset_index(drop="index", inplace=True)
print(df.shape)

"""
df.sort_values(by=1, inplace = True)
for _ in range(df.shape[0]):
    print("iteration n°", _)
    df = get_all_ranges_overlapping(df)
    df.sort_values(by=0, inplace=True)
print(df)
"""

df.to_csv("day_5.csv")
df["+1"] = df[1]+1
print(sum(df["+1"]-df[0]))

# total_fresh_ranges = []
# for i in range(df.shape[0]):
#     total_fresh_ranges.append(df.loc[i, 1]+1 - df.loc[i, 0])

# print((total_fresh_ranges))
# print(sum(total_fresh_ranges))





# 372759287730410
# 370192515053777
# 370 192 515 053 777
# 369 993 886 244 502

# is too high

# 344 322 275 609 331 not the right answer
# 344 322 275 609 198 not the right answer
# 344 322 275 609 331

# il faut tweeker le code pour sort by col "1" en ordonné aussi
# 344123646800056
# 304 381 322 684 534 not the correct answer
# 304 381 322 684 534
# 353 376 608 341 030
# 387 392 299 327 819
