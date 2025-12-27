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
            new_series = pd.to_numeric(df[col], errors="coerce")
            dff[col] = new_series


        s = pd.Series((dff.isna().sum() == dff.shape[0]))
        separation_columns = (list(s[s==True].index))

        return df, separation_columns
    elif modality == "index":
        dff = df.copy()

        for idx in df.index:
            new_series = pd.to_numeric(dff.loc[idx, :], errors="coerce")
            dff.loc[idx, :] = new_series

        s = pd.Series(((dff.T).isna().sum() == dff.shape[1]))
        separation_columns = (list(s[s==True].index))

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

        for col_idx in range(len(separation_columns)-1):
            sep_avant = separation_columns[col_idx]
            sep_apres = separation_columns[col_idx+1]

            cephalopod_math = []

            for idx in range(until_last_num):
                cephalopod_math.append(int(''.join(list(df.loc[idx, sep_avant:(sep_apres-1)]))))

            if sep_avant != 0:
                sign = df.loc[until_last_num,sep_avant+1]
            else:
                sign = df.loc[until_last_num,sep_avant]
            consolidated_maths.append([cephalopod_math, sign])


    return df, separation_columns, consolidated_maths

def answer_part_1(my_input="day_6.txt"):
    my_input = open(my_input, "r").read()
    new = my_input.split("\n")
    df = create_df(new)

    df, separation_columns = get_separation_columns(df)
    df, separation_columns, consolidated_maths = extract_numbers_and_signs(df, separation_columns)

    total = []
    for elem in range(len(consolidated_maths)):
        nums_list = (consolidated_maths[elem][0])
        sign = (consolidated_maths[elem][1])

        if sign == "+":
            total.append(sum(nums_list))
        elif sign == "*":
            total.append(math.prod(nums_list))

    print(sum(total))

print("answer_part_1:")
answer_part_1("example_day_6.txt")
print("---"*3)
answer_part_1()

print()
# --------------- Part 2 --------------
def setup(text_file="example_day_6.txt"):
    my_input = open(text_file, "r").read()
    new = my_input.split("\n")
    df = create_df(new)
    df = (df.T)
    df, separation_lines = get_separation_columns(df, modality="index")
    df, separation_lines = clean_df_and_sep_columns(df, separation_lines, modality="index")
    return df

def get_list_of_nb(text_file="example_day_6.txt"):
    df = setup(text_file)
    df_bis = df[list(df.columns)[:-1]]

    my_list = []
    big_list = []
    idx_start = 0

    while idx_start != df.shape[0]:
        my_list = []
        for idx in range(idx_start, df.shape[0]):
            if ("".join(df_bis.loc[idx, :])).strip() != "":
                my_list.append(int("".join(df_bis.loc[idx, :])))
            else:
                break
        my_list.append((df.loc[idx_start, df.columns[-1]]))
        big_list.append(my_list)
        idx_start = idx + 1
    return big_list

def get_result_2(text_file="example_day_6.txt"):

    df = setup(text_file)
    big_list = get_list_of_nb(text_file)
    # print(big_list)

    total = []
    for elem in range(len(big_list)):
        nums_list = (big_list[elem][:-1])
        sign = (big_list[elem][-1])

        if sign == "+":
            total.append(sum(nums_list))
        elif sign == "*":
            total.append(math.prod(nums_list))

    print(sum(total))

print("answer_part_2:")
get_result_2()
print("---"*3)
get_result_2("day_6.txt")
