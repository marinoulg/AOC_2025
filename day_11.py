def recursive_temp(my_dict, key="svr"):
    """
    returns a list of lists (each new list is the child of a node, if comparing to a decision tree)
    compiling each possible way.
    as it is recursive and we create a new list called pair_of_keys at each new iteration of the recursivity,
    we have lists inside of lists.
    """
    pair_of_keys = []
    for key in my_dict[key]:
        pair_of_keys.append(key)

        while key != 'out':
            key = recursive_temp(my_dict, key)
            pair_of_keys.append(" ".join(key))
            break

    return pair_of_keys

def get_all_possibilities(my_dict, key="svr"):
    """
    returns a proper list of each possible path, from "start" to "out".
    """

    pair_of_keys = recursive_temp(my_dict, key)

    all_lists = []

    for elem in pair_of_keys:
        if len(elem)==3:
            temp = elem + " "
        else:
            splitted = elem.split("out")

            temp_list = []
            for elems in range(len(splitted)):
                if len(temp + splitted[elems]) > 4:
                    to_append = ("you " + temp + splitted[elems] + "out").replace("  ", " ").replace(" ", ",")
                    temp_list.append(to_append)

            all_lists.append(temp_list)

    lists_1D = []
    for elem in all_lists:
        if isinstance(elem, list):
            for el in elem:
                print(el)
                lists_1D.append(el)

    return lists_1D

def answer_part_1(text_file= "example_day_11.txt", key="svr"):
    """
    compiles all steps to return the answer, aka the length of the 1D-list compiled.
    """
    my_input = open(text_file, "r").read()
    new = my_input.split("\n")[:-1]

    my_dict = {}
    for i in range(len(new)):
        temp = (new[i].split(": "))
        my_dict[temp[0]] = temp[1].split(" ")

    lists_1D = get_all_possibilities(my_dict, key)
    return len(lists_1D)
