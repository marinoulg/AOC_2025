import pandas as pd

def get_sizes_of_gifts(text_file = "example_day_12.txt"):
    my_input = open(text_file, "r").read()
    indexes = my_input.replace("\n\n", "\naaa").split("aaa")[-1]
    indexes = indexes.split("\n")

    indexes_for_gifts = []
    sizes_of_gifts = []
    for index in indexes[:-1]:
        a, b = (index.split(":")[0].split("x"))
        sizes_of_gifts.append((int(a), int(b)))

        tmp = []
        for elem in index.split(" ")[1:]:
            tmp.append(int(elem))

        indexes_for_gifts.append(tmp)

    return indexes_for_gifts, sizes_of_gifts

def get_gifts_shape(text_file = "example_day_12.txt"):
    my_input = open(text_file, "r").read()
    gifts_temp = my_input.replace("\n\n", "\naaa").split("aaa")[:-1]

    gifts_ = {}
    for gift in gifts_temp:
        gifts_[gift.split("\n")[0]] = gift.split("\n")[1:-1] # 1 to not start "0:" etc. bc pandas' columns is the same

    gifts = {}
    gifts_temp = list(gifts_.values())
    for i in range(len(gifts_temp)):
        gift_1 = list()
        for elem in gifts_temp[i]:
            tmp = []
            for char in elem:
                tmp.append(char)
            gift_1.append(tmp)

        gifts[i] = gift_1

    return gifts

def setting_up_perimeter_of_challenge(index, text_file = "example_day_12.txt"):
    """
    if I want to see for index '0' of shapes of gifts and
    of room behind the tree of index '0'

    ex: index = 2
    --> goes from 0 to (len(indexes_for_gifts)-1)

    """
    gifts = get_gifts_shape(text_file)
    indexes_for_gifts, sizes_of_gifts = get_sizes_of_gifts(text_file)


    # Print the indexes of the gifts whose shape we will try to fit below the tree
    tmp_df = pd.DataFrame(indexes_for_gifts[index]).T
    print(tmp_df)
    print()

    print("indexes of gifts to be put below the tree: ", end='')
    shapes = []
    for y in (tmp_df.columns):
        if tmp_df.loc[0,y] != 0:
            print(y, end='; ')
            shapes.append(y)

    print(end="\n\n")
    # Print the shape of the tree available
    x,y = sizes_of_gifts[index]
    print(pd.DataFrame([['.']*x]*y))
    print()

    # Print the look/shape of each gift
    for gift_idx in shapes:
        print(f"{tmp_df.loc[0,gift_idx]} gift{"s" if tmp_df.loc[0,gift_idx]>1 else ""} of index {gift_idx}")
        print(pd.DataFrame(gifts[gift_idx]))
        print()


if __name__ == "__main__":
    setting_up_perimeter_of_challenge(1)
