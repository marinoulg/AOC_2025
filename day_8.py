import numpy as np
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt

def get_all_tuples(text_file = "example_day_8.txt"):
    """
    this function creates a list of tuples from the given input.
    currently used
    """
    my_input = open(text_file, "r").read()
    new = my_input.split("\n")[:-1]

    all_tuples = []

    for i in range(len(new)):
        my_tuple = []
        for elem in new[i].split(','):
            my_tuple.append(int(elem))

        all_tuples.append(tuple(my_tuple))
    print("STEP 1 DONE - all tuples created")
    return all_tuples

def get_result(G):
    """
    currently used
    """
    components = list(nx.connected_components(G))
    print(components)
    all_lengths = ([len(c) for c in components])

    first = max(all_lengths)
    all_lengths.remove(max(all_lengths))
    second = max(all_lengths)
    all_lengths.remove(max(all_lengths))
    third = max(all_lengths)

    print("STEP 5 DONE - result computed")

    return first * second * third

def get_distances_sorted(all_tuples, k=None):
    all_distances_set = set()
    all_distances_tuples_dict = defaultdict(list)

    for j in range(len(all_tuples)):
        comparison_tuple = all_tuples[j]

        for i in range(len(all_tuples)):
            if all_tuples[i] != comparison_tuple:
                dx = comparison_tuple[0] - all_tuples[i][0]
                dy = comparison_tuple[1] - all_tuples[i][1]
                dz = comparison_tuple[2] - all_tuples[i][2]
                dist = np.sqrt(dx*dx + dy*dy + dz*dz)


                temp = (comparison_tuple, all_tuples[i])
                all_distances_tuples_dict[dist].append(temp)
                all_distances_set.add(dist)

    print("STEP 2 DONE - all distances tuples and set created")

    sorted_list = sorted(all_distances_set)[:k]
    print(f"STEP 3 DONE - a list of {k if k != None else "all the ranked"} shortest distances created")
    return sorted_list, all_distances_tuples_dict



def answer_part_1(text_file="example_day_8.txt", k=10):
    """
    in this function, it constructs the graph and gets the result from another function
    """
    all_tuples = get_all_tuples(text_file)
    sorted_list, all_distances_tuples_dict = get_distances_sorted(all_tuples, k)

    G = nx.Graph()

    for i in range(len(sorted_list)):
        for node1, node2 in all_distances_tuples_dict[sorted_list[i]]:
            G.add_edge(node1, node2, label=sorted_list[i])
            # nx.draw(G, with_labels=True)
            # plt.show()

    print("STEP 4 DONE - Knowledge Graph defined")

    res = get_result(G)
    return res

print(answer_part_1("day_8.txt", k=1000))

# ------------------- Part 2 ---------------------

def get_both_tuples_that_reunite_components(text_file="example_day_8.txt"):
    all_tuples = get_all_tuples(text_file)
    sorted_list, all_distances_tuples_dict = get_distances_sorted(all_tuples)

    G = nx.Graph()

    k = len(all_tuples)
    iteration = 0
    for i in range(len(sorted_list)):
        node1, node2 = all_distances_tuples_dict[sorted_list[i]][0]
        G.add_edge(node1, node2)
        if len(list(nx.connected_components(G))[0]) == k:
            print(iteration)
            return (node1, node2)
        iteration+=1
    # nx.draw(G, with_labels=True)
    # plt.show()

    print(nx.number_connected_components(G))

def get_answer_part2(text_file="example_day_8.txt"):
    n1, n2 = get_both_tuples_that_reunite_components(text_file)
    return n1[0]*n2[0]

print(get_answer_part2("day_8.txt"))
