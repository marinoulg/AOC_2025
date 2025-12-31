import pandas as pd
import numpy as np
import networkx as nx
import math
from collections import defaultdict

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

def compare_distance_two_pairs(pair_1, pair_2):
    # pair_1 = all_tuples[0]
    # pair_2 = all_tuples[1]

    xa, ya, za = pair_1
    xb, yb, zb = pair_2

    return np.sqrt((xa-xb)**2+(ya-yb)**2+(za-zb)**2)

def get_dict_comparing_all_coordinates(all_tuples):

    smallest_distances = {}
    iteration = 1

    for j in range(len(all_tuples)):
        pair1 = all_tuples[j]

        for i in range(len(all_tuples)):
            if i != j:
                # print(f"comparing pair1:{all_tuples[j]} and pair2:{all_tuples[i]}")
                pair2=all_tuples[i]
                comparison = (compare_distance_two_pairs(pair1, pair2))
                if comparison not in smallest_distances:
                    smallest_distances[comparison]=sorted([(pair1, pair2)])

                # print(f"iteration n°{iteration}")
                iteration+=1

    print("STEP 2 DONE - creating a dictionary of all distances according to the comparison of coordinates with each other")

    return smallest_distances

def get_ten_smallest_distances_for_KG(smallest_distances):

    smallest_distances_for_graph = []

    for key, value in smallest_distances.items():
        for i in range(10):
            if key == sorted((smallest_distances.keys()))[i]:
                temp = [value[0][0], value[0][1], key]
                smallest_distances_for_graph.append(temp)
                next

    print("STEP 3 DONE - we have selected the 10 smallest distances")

    return smallest_distances_for_graph

def create_KG(smallest_distances_for_graph):
    G = nx.Graph()
    for i in range(len(smallest_distances_for_graph)):
        node_1 = smallest_distances_for_graph[i][0]
        node_2 = smallest_distances_for_graph[i][1]
        result = smallest_distances_for_graph[i][2]

        G.add_edge(node_1, node_2, label=result)

        if (i+1) == 10:
            # Visualize the knowledge graph
            pos = nx.spring_layout(G, seed=42, k=0.9)
            labels = nx.get_edge_attributes(G, 'label')
            # plt.figure(figsize=(12, 10))
            # nx.draw(G, pos, with_labels=True, font_size=10, node_size=700, node_color='lightblue', edge_color='gray', alpha=0.6)
            # nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, label_pos=0.3, verticalalignment='baseline')
            # plt.title('Knowledge Graph')
            # plt.show()
            break

    print("STEP 4 DONE - Knowledge Graph has been created")

    return G

def get_result(G):
    """
    currently used
    """
    components = list(nx.connected_components(G))
    all_lengths = ([len(c) for c in components])

    first = max(all_lengths)
    all_lengths.remove(max(all_lengths))
    second = max(all_lengths)
    all_lengths.remove(max(all_lengths))
    third = max(all_lengths)

    print("STEP 5 DONE - result computed")

    return first * second * third

def answer_part_(text_file= "example_day_8.txt"):
    all_tuples = get_all_tuples(text_file )
    smallest_distances = get_dict_comparing_all_coordinates(all_tuples)
    smallest_distances_for_graph = get_ten_smallest_distances_for_KG(smallest_distances)
    G = create_KG(smallest_distances_for_graph)
    return get_result(G)

# ----------------- Part 1 -----------------


def answer_part_1(text_file="example_day_8.txt"):
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

    sorted_list = sorted(all_distances)[:10]
    print("STEP 3 DONE - a list of 10 shortest distances created")

    # def create_KG(shortest_distances, sorted_list):
    G = nx.Graph()

    for i in range(len(sorted_list)):
        # temp_list = all_distances_tuples[sorted_list[i]]
        for node1, node2 in all_distances_tuples[sorted_list[i]]:

        # if (temp_list[0] == temp_list[-1]) and (temp_list[1] == temp_list[2]):
        #     node1, node2 = temp_list
            G.add_edge(node1, node2, label=sorted_list[i])
        # elif len(temp_list) > 2:
        #     print(temp_list)

    print("STEP 4 DONE - Knowledge Graph defined")

    res = get_result(G)
    return res

print(answer_part_1("day_8.txt"))
