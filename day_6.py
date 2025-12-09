import pandas as pd
import math

my_input = open("example_day_6.txt", "r").read()
new = my_input.split("\n")

# print(new)
# --------------- My functions --------------

def create_df(new):
    df = []
    for x in range(len(new)-1):
        temp = []
        for i in new[x]:
            temp.append(i)
        df.append(temp)

    df = (pd.DataFrame(df))
    # print(df)
    return df

def get_separation_columns(df, modality="column"):
    """
    the goal here is to get the columns' names (here, their idx number)
    associated with the separations of the numbers

    NB: for part 2, we have realised that these will remained unchanged because the df remains
    the same no matter if we deal with it like in part 1 (in columns), or like in part 2 (in index).
    """
    if modality=="column":
        dff = df.copy()

        for col in df.columns:
            # print(col)
            new_series = pd.to_numeric(df[col], errors="coerce")
            dff[col] = new_series


        s = pd.Series((dff.isna().sum() == dff.shape[0]))
        separation_columns = (list(s[s==True].index))
        # print("separation_columns:", separation_columns)

        return df, separation_columns
    elif modality == "index":
        dff = df.copy()

        for idx in df.index:
            new_series = pd.to_numeric(dff.loc[idx, :], errors="coerce")
            dff.loc[idx, :] = new_series

        s = pd.Series(((dff.T).isna().sum() == dff.shape[1]))
        separation_columns = (list(s[s==True].index))
        # print(separation_columns)
        return df, separation_columns

def clean_df_and_sep_columns(df, separation_columns, modality="column"):
    for col in df.columns:
        df[col] = df[col].fillna(" ") # fix None on last column

    if modality=="column":
        separation_columns.insert(0,0) # insert in list the first column which is the start of the separation
        separation_columns.insert(df.shape[1]-1, df.shape[1]) # same for last one
    elif modality == "index":
        separation_columns.insert(0,0) # insert in list the first line which is the start of the separation
        separation_columns.insert(df.shape[0]-1, df.shape[0]-1) # same for last one

    return df, separation_columns

def extract_numbers_and_signs(df, separation_columns, modality="column"):
    """
    using the cleaned df and the clean separation_columns, we extract in this function
    the integers in the df along with their sign (as a string)

    Semantics:
        - until_last_num: column (or line) that is filled with blank spaces and "+" or "*"
        - sep_avant: lower bound of the interval (evolving)
        - sep_apres: upper bound of the interval (evolving)
    """
    df, separation_columns = clean_df_and_sep_columns(df, separation_columns)

    consolidated_maths = []

    if modality == "column":
        until_last_num = (df.shape[0]-1)
        print("until_last_num:", until_last_num)

        for col_idx in range(len(separation_columns)-1):
            sep_avant = separation_columns[col_idx]
            sep_apres = separation_columns[col_idx+1]
            print("sep_avant:", sep_avant)
            print("sep_apres:", sep_apres)

            cephalopod_math = []
            # sign = str()
            for idx in range(until_last_num):
                # idx = 2
                print(df.loc[idx:until_last_num, sep_avant:(sep_apres-1)])
                cephalopod_math.append(int(''.join(list(df.loc[idx, sep_avant:(sep_apres-1)]))))

            print("cephalopod_math:", cephalopod_math)
            if sep_avant != 0:
                sign = df.loc[until_last_num,sep_avant+1]
            else:
                sign = df.loc[until_last_num,sep_avant]
            print("sign:", sign)
            print()
            consolidated_maths.append([cephalopod_math, sign])

    elif modality == "index":
        until_last_num = (df.shape[1]-1)




    return df, separation_columns, consolidated_maths


def answer_part_1(my_input="day_6.txt"):
    my_input = open(my_input, "r").read()
    new = my_input.split("\n")
    df = create_df(new)
    # print(df)

    df, separation_columns = get_separation_columns(df)
    df, separation_columns, consolidated_maths = extract_numbers_and_signs(df, separation_columns)

    total = []
    for elem in range(len(consolidated_maths)):
        nums_list = (consolidated_maths[elem][0])
        print(nums_list)
        sign = (consolidated_maths[elem][1])
        print(sign)
        if sign == "+":
            total.append(sum(nums_list))
        elif sign == "*":
            total.append(math.prod(nums_list))

    print(sum(total))

# answer_part_1("example_day_6.txt")
# print("---"*3)
# answer_part_1()

# --------------- Part 2 --------------
df = create_df(new)
df = (df.T)
df, separation_lines = get_separation_columns(df, modality="index")
print(df)

df, separation_lines = clean_df_and_sep_columns(df, separation_lines, modality="index")
print(separation_lines)



consolidated_maths = []
"""
Semantics:
        - until_last_num: column (or line) that is filled with blank spaces and "+" or "*"
        - sep_avant: lower bound of the interval (evolving)
        - sep_apres: upper bound of the interval (evolving)
"""

until_last_num = (df.shape[1]-1)-1 # -1 bc we start at 0, and -1 bc we discount the last column in this case
print("until_last_num:", until_last_num)
print("my test")

sep_upper = 3
sep_lower = 7

print((df.loc[sep_upper:sep_lower,:until_last_num]))
print()
print(int(''.join(df.loc[sep_upper+1,:until_last_num])))


for idx in range(len(separation_lines)-1):

    sep_upper= separation_lines[idx]
    sep_lower = separation_lines[idx+1]
    print("sep_upper:", sep_upper)
    print("sep_lower:", sep_lower)


    cephalopod_math = []
    sign = str()
    print(int(''.join(df.loc[sep_upper+1,:until_last_num])))

    # for col in range((df.shape[1]-1)):
    #     print(col)
    # #     # idx = 2
    #     print(df.loc[idx:col, sep_avant:(sep_apres-1)])
    #     cephalopod_math.append(int(''.join(list(df.loc[idx, sep_avant:(sep_apres-1)]))))

    # print("cephalopod_math:", cephalopod_math)
    # if sep_avant != 0:
    #     sign = df.loc[until_last_num,sep_avant+1]
    # else:
    #     sign = df.loc[until_last_num,sep_avant]
    # print("sign:", sign)
    print()
    # consolidated_maths.append([cephalopod_math, sign])
