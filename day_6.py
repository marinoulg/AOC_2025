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

def get_separation_columns(df):
    """
    the goal here is to get the columns' names (here, their idx number)
    associated with the separations of the numbers
    """
    dff = df.copy()
    for col in df.columns:
        # print(col)
        new_series = pd.to_numeric(df[col], errors="coerce")
        dff[col] = new_series


    s = pd.Series((dff.isna().sum() == dff.shape[0]))
    separation_columns = (list(s[s==True].index))
    # print("separation_columns:", separation_columns)

    return df, separation_columns

def clean_df_and_sep_columns(df, separation_columns):
    for col in df.columns:
        df[col] = df[col].fillna(" ") # fix None on last column

    separation_columns.insert(0,0) # insert in list the first column which is the start of the separation
    separation_columns.insert(df.shape[1]-1, df.shape[1])
    # print("separation_columns:", separation_columns)

    until_last_num = (df.shape[0]-1)
    # print("until_last_num:", until_last_num)
    # print("---"*5)
    return df, separation_columns

def extract_numbers_and_signs(df, separation_columns):
    """
    using the cleaned df and the clean separation_columns, we extract in this function
    the integers in the df along with their sign (as a string)
    """
    df, separation_columns = clean_df_and_sep_columns(df, separation_columns)
    until_last_num = (df.shape[0]-1)

    consolidated_maths = []
    for col_idx in range(len(separation_columns)-1):
        sep_avant = separation_columns[col_idx]
        sep_apres = separation_columns[col_idx+1]
        # print("sep_avant:", sep_avant)
        # print("sep_apres:", sep_apres)

        cephalopod_math = []
        # sign = str()
        for idx in range(until_last_num):
            # idx = 2
            # print(df.loc[idx:until_last_num, sep_avant:(sep_apres-1)])
            cephalopod_math.append(int(''.join(list(df.loc[idx, sep_avant:(sep_apres-1)]))))

        # print("cephalopod_math:", cephalopod_math)
        if sep_avant != 0:
            sign = df.loc[until_last_num,sep_avant+1]
        else:
            sign = df.loc[until_last_num,sep_avant]
        # print("sign:", sign)
        # print()
        consolidated_maths.append([cephalopod_math, sign])

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

answer_part_1("example_day_6.txt")
print("---"*3)
answer_part_1()
