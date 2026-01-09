import networkx as nx
import matplotlib.pyplot as plt

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

# ---------------- Part 2 ----------------

def get_all_paths_from_svr_to_out(my_dict):

    G = nx.DiGraph()

    for i in range(len(list(my_dict.keys()))):
        key = (list(my_dict.keys())[i])
        for elem in my_dict[key]:
            G.add_edge(key, elem)

    from_svr_to_out = list(nx.all_simple_paths(G, "svr", "out"))
    return from_svr_to_out

def answer_part_2(text_file= "example_day_11_2.txt", key="svr"):

    my_input = open(text_file, "r").read()
    new = my_input.split("\n")[:-1]

    my_dict = {}
    for i in range(len(new)):
        temp = (new[i].split(": "))
        my_dict[temp[0]] = temp[1].split(" ")

    from_svr_to_out = get_all_paths_from_svr_to_out(my_dict)

    count = 0
    for list_ in from_svr_to_out:
        if "dac" in list_:
            if "fft" in list_:
                print(list_)
                count+=1

    return count


# ---------------- Old code ----------------

def get_tree_options(text_file= "example_day_11_p2.txt"):

    my_input = open(text_file, "r").read()
    new = my_input.split("\n")[:-1]

    my_dict = {}
    for i in range(len(new)):
        temp = (new[i].split(": "))
        my_dict[temp[0]] = temp[1].split(" ")

    tree = recursive_temp(my_dict, key="svr")
    aa = [tree]
    aa.insert(0, "svr")

    return tree # aa ?

def get_1D_options(text_file= "example_day_11_p2.txt"):
    """
    la logique c'est :
    si juste derrière y'a une liste, juste avant y'a un node

    WIP
    """
    tree = get_tree_options(text_file)


# Possibilities ?


def get_first_nodes(tree):
    nodes = []
    for i in range(len(tree)-1):
        if isinstance(tree[i+1], list):
            nodes.append(tree[i])
        # else:
        #     print(tree[i+1])
    return nodes

def get_nodes_after(tree):
    nodes = []
    for i in range(len(tree)):
        for j in range(len(tree[i])-1):
            if isinstance(tree[i][j+1], list):
                nodes.append(tree[i][j])
        # else:
        #     print(tree[i+1])
    return nodes


# text_file= "example_day_11_p2.txt"

# my_input = open(text_file, "r").read()
# new = my_input.split("\n")[:-1]

# my_dict = {}
# for i in range(len(new)):
#     temp = (new[i].split(": "))
#     my_dict[temp[0]] = temp[1].split(" ")

# tree = recursive_temp(my_dict, key="svr")

# nodes = get_first_nodes(tree)
# print("nodes 1", nodes)

# new_tree = tree.copy()
# for elem in new_tree:
#     if elem in nodes:
#         new_tree.remove(elem)

# nodes = get_nodes_after(new_tree)
# print("nodes 2", nodes)
