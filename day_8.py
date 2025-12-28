import pandas as pd
import numpy as np
import networkx as nx

def get_all_tuples(text_file = "example_day_8.txt"):
    """
    this function creates a list of tuples from the given input.
    it could be useful if we wanted to know the tuples that are alone after 9 iterations (eg, there are 7 in the provided example).
    """
    my_input = open(text_file, "r").read()
    new = my_input.split("\n")[:-1]

    all_tuples = []

    for i in range(len(new)):
        my_tuple = []
        for elem in new[i].split(','):
            my_tuple.append(int(elem))

        all_tuples.append(tuple(my_tuple))
    return all_tuples


def create_lists_for_x_y_z(text_file="example_day_8.txt"):
    """
    this function creates separated lists for X, Y and Z
    and allows for a DataFrame to be created
    """
    my_input = open(text_file, "r").read()
    new = my_input.split("\n")[:-1]

    X_s = []
    Y_s = []
    Z_s = []
    for elem in new[:-1]:
        x, y, z = (elem.split(','))
        X_s.append(int(x))
        Y_s.append(int(y))
        Z_s.append(int(z))
    return X_s, Y_s, Z_s


def compare_one_with_all(one_idx, text_file="example_day_8.txt"):
    """
    this functions allows to compare distances between 1 cordinate and the others to know the closest one
    - discontinued
    """
    my_input = open(text_file, "r").read()

    X_s, Y_s, Z_s = create_lists_for_x_y_z(text_file)
    x_compared, y_compared, z_compared = X_s[one_idx], Y_s[one_idx], Z_s[one_idx]

    results = []
    indexes = []

    result = int()
    index = int()
    temps = {}
    for idx in range(len(X_s)):
        x3 = X_s[idx]
        y3 = Y_s[idx]
        z3 = Z_s[idx]

        temp = np.sqrt((x3-x_compared)**2+(y3-y_compared)**2+(z3-z_compared)**2)
        temps[idx] = temp

        if idx == 0:
            result = temp
            index = idx
        elif (temp < result) and (temp != 0):
            result = temp
            index = idx
        results.append(temp)
        indexes.append(idx)
    return index, result, temps # , results, indexes



def get_ten_smallest_results(text_file="example_day_8.txt"):
    """
    this function creates the first DataFrame to be used in the knowledge graph.
    """
    my_input = open(text_file, "r").read()

    X_s, Y_s, Z_s = create_lists_for_x_y_z(text_file)

    df = pd.DataFrame()

    for idx in range(len(X_s)):
        index, result, temps  = (compare_one_with_all(idx, text_file))
        df_1 = pd.DataFrame([temps.keys(), temps.values()]).T
        df_1["index"] = idx
        df_1 = df_1.rename(columns={0:"compared_with", 1:"result"})
        df_1 = df_1[["index", "compared_with", "result"]]
        df_1
        df = pd.concat([df, df_1])

    df.compared_with = df.compared_with.astype(int)

    df = df.sort_values(by="result")
    df = df[df["result"] != 0]

    def get_coordinates_per_index(index):
        x = X_s[index]
        y = Y_s[index]
        z = Z_s[index]
        return (x,y,z)

    df["coords_index"] = df["index"].apply(get_coordinates_per_index)
    df["coords_compared_with"] = df["compared_with"].apply(get_coordinates_per_index)

    df = df.reset_index()
    df = df.drop(columns="level_0")

    print("ten smallest created")

    return df



def get_df_clean(text_file="example_day_8.txt"):
    """
    this function creates the final DataFrame to be used in the knowledge graph.
    """
    my_input = open(text_file, "r").read()

    df = get_ten_smallest_results(text_file).head(40)

    to_drop = []
    for idx in range(df.shape[0]):
        if idx%2==0:
            to_drop.append(idx)

    for idx in to_drop:
        df.drop(index=idx, inplace=True)

    df = df.reset_index().drop(columns="level_0")

    print("df clean created")

    return df


def create_KG(text_file="example_day_8.txt"):
    """
    this function creates a graph to be used for the counting of the nodes and edges
    """
    df = get_df_clean(text_file)
    # Create a knowledge graph
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row['coords_index'], row['coords_compared_with'], label=row['result'])

        if (_+1) == 9:
            # Visualize the knowledge graph
            pos = nx.spring_layout(G, seed=42, k=0.9)
            labels = nx.get_edge_attributes(G, 'label')
            # plt.figure(figsize=(12, 10))
            # nx.draw(G, pos, with_labels=True, font_size=10, node_size=700, node_color='lightblue', edge_color='gray', alpha=0.6)
            # nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, label_pos=0.3, verticalalignment='baseline')
            # plt.title('Knowledge Graph')
            # plt.show()
            break

    print("KG created")

    return G

def get_all_possible_connections(text_file="example_day_8.txt"):
    """
    this function creates a list of lists filled with tuples (x,y,z) of coordinates that are linked together,
    either directly or indirectly
    """
    G = create_KG(text_file)

    those_that_are_used = list(G.nodes)

    connections = []
    for key, value in dict(G.degree).items():
        temp = []
        if value > 1:
            temp.append(key)
            # print(key)
            for node in those_that_are_used:
                if G.has_edge(u=key,v=node):
                    # print(node)
                    if node not in temp:
                        temp.append(node)
            connections.append(temp)

    # print(connections)

    all_connections = []
    temp_to_compare = []
    for comparing in range(len(connections)):
        conn_comparing = connections[comparing].copy()

        for iterable in range(len(connections)):
            conn_i = connections[iterable]

            for i in range(len(conn_i)):
                if conn_comparing[0] == conn_i[i]:
                    for elem in (conn_i):
                        if elem not in conn_comparing:
                            conn_comparing.append(elem)

        if sorted(conn_comparing) not in all_connections:
            all_connections.append(sorted(conn_comparing))

            for elem in conn_comparing:
                temp_to_compare.append(elem)

    for elem in list(dict(G.degree).keys()):
        if elem not in temp_to_compare:
            # print(sorted(list(sorted(list(G.edges(elem)))[0])))
            sorting = sorted(list(sorted(list(G.edges(elem)))[0]))
            if sorting not in all_connections:
                all_connections.append(sorting)

    print("all possible connections created")

    return all_connections


def answer_part_1(text_file="example_day_8.txt"):
    """
    this function prints out the result of the three biggest number of connections (direct or not)
    within the graph we have built.
    """
    all_connections = get_all_possible_connections(text_file)

    lengths = []
    for i in range(len(all_connections)):
        lengths.append(len(all_connections[i]))

    print(lengths)

    first = max(lengths)
    lengths.remove(max(lengths))

    second = max(lengths)
    lengths.remove(max(lengths))

    third = max(lengths)

    return first * second * third

print(answer_part_1("day_8.txt"))
print(create_KG("day_8.txt"))
