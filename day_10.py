import pandas as pd

def starting_off(text_file = "example_day_10.txt"):
    my_input = open(text_file, "r").read()
    new = my_input.split("\n")[:-1]

    light_diagrams = []
    wiring_schematics = []
    joltages = []

    for line in new:
        temp = (line.split(" "))
        light_diagrams.append(temp[0])
        wiring_schematics.append(temp[0+1:-1])

        joltages.append(temp[-1]) # irrelevant and can safely be ignored

    what_I_want = pd.DataFrame([[light_diagrams[i][j] for j in range(1, len(light_diagrams[i])-1)] for i in range(len(light_diagrams))])
    return light_diagrams, wiring_schematics, joltages, what_I_want

def get_beginning(what_I_want):
    beginning = what_I_want.copy()
    for x in range(beginning.shape[0]):
        for y in range(beginning.shape[1]):
            if isinstance(beginning.loc[x,y], str): # and beginning.loc[x,y] not in ["[","]"]:
                beginning.loc[x,y] = '.'
    return beginning

def get_toggles(what_I_want):
    """
    the rationale behind this function is that each button needs to be pressed
    either an even or an odd number of times, depending on if it needs to be off
    or on at the end.
        --> buttons that need to be on are "impair" as all button start as off
        --> buttons that need to be off are "pair" as all button start as off
    """
    beginning = get_beginning()

    toggles = []
    for line in range(what_I_want.shape[0]):
        # line = 0
        temp = {}
        impair_nb_of_toggles = []
        pair_nb_of_toggles = []
        for value, idx in zip((beginning.loc[line,:] == what_I_want.loc[line,:]).values, (beginning.loc[line,:] == what_I_want.loc[line,:]).index):
            if value == False:
                impair_nb_of_toggles.append(idx)
            else:
                pair_nb_of_toggles.append(idx)

        temp["impair"] = impair_nb_of_toggles
        temp["pair"] = pair_nb_of_toggles

        toggles.append(temp)
    return toggles
