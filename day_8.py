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

# print(get_all_tuples())

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


def answer_part_1(text_file="example_day_8.txt", k=10):
    """
    half working - only on example --> needs to include all antinodes now
        "geometry → integer vector stepping → set of points"

    mid-work of all current steps (granted, could be better organised)
    followed to get to the solution
    """

    all_tuples = get_all_tuples(text_file)

    all_distances = set()
    all_distances_tuples = defaultdict(list)

    # def get_ten_shortest_distances(text_file = "example_day_8.txt"):
    for j in range(len(all_tuples)):
        comparison_tuple = all_tuples[j]

        for i in range(len(all_tuples)):
            if all_tuples[i] != comparison_tuple:
                # dist = (math.dist(comparison_tuple, all_tuples[i]))
                dx = comparison_tuple[0] - all_tuples[i][0]
                dy = comparison_tuple[1] - all_tuples[i][1]
                dz = comparison_tuple[2] - all_tuples[i][2]
                dist = np.sqrt(dx*dx + dy*dy + dz*dz)

                all_distances_tuples[dist].append((comparison_tuple, all_tuples[i]))
                all_distances.add(dist)

    print("STEP 2 DONE - all distances tuples and set created")
    # print(all_distances_tuples)

    sorted_list = sorted(all_distances)[:k]
    print("STEP 3 DONE - a list of 10 shortest distances created")

    # def create_KG(shortest_distances, sorted_list):
    G = nx.Graph()

    for i in range(len(sorted_list)):
        # temp_list = all_distances_tuples[sorted_list[i]]
        for node1, node2 in all_distances_tuples[sorted_list[i]]:
            # print(all_distances_tuples[sorted_list[i]])

        # if (temp_list[0] == temp_list[-1]) and (temp_list[1] == temp_list[2]):
        #     node1, node2 = temp_list
            G.add_edge(node1, node2, label=sorted_list[i])
        # elif len(temp_list) > 2:
        #     print(temp_list)
            nx.draw(G, with_labels=True)
            plt.show()

    print("STEP 4 DONE - Knowledge Graph defined")

    res = get_result(G)
    return res

# print(answer_part_1("example_day_8.txt", k=1000))


# components = list(nx.connected_components(G))
# print(components)
