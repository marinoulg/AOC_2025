# ------------ Part 1 ------------
def find_elem(elem, str_to_be_found):
    """
    permet de chercher un caractère particulier dans une suite de caractères
    ex : chercher "9" dans "123456789"
    """
    for i in range(len(elem)):
        if elem[i] == str_to_be_found:
            reminder = (len(elem)-i) - 1
            if reminder != 0:
                return elem[i+1:], reminder
            else:
                return str(), reminder
        else:
            next
    return 0

def find_biggest_two(elem):
    """
    default value : elem = updated_input[0]
    """
    first_line = []

    for num in range(9, -1, -1):
        if str(num) in elem:
            new_elem, reminder = find_elem(elem,
                    str(num))

            if len(new_elem) > 0:
                first_line.append(str(num))
                for i in range(9, -1, -1):
                    if find_elem(new_elem, str(i)) != None:
                        first_line.append(str(i))
            else:
                next

    return int(first_line[0]+first_line[1])

def result_1(text_file = "example_day_3.txt"):
    my_input = open(text_file, "r").read()

    updated_input = my_input.split("\n")[:-1]

    result_p1 = list()
    for i in range(len(updated_input)-1):
        result_p1.append((find_biggest_two(updated_input[i])))

    return sum(result_p1)

print("Part 1:", result_1("day_3.txt"))

# ------------ Part 2 ------------

def test_len_and_possibility(elem, length_next=10):
    """
    permet de tester quel est le plus haut chiffre (en string) d'une chaîne de caractères,
    tout en voyant le nombre de caractères qui suivent ce plus haut chiffre.
    si la suite de caractères est bien supérieure à length_next, alors on considère qu'on
    a trouvé le plus haut chiffre dont la suite est possible, sinon on continue à chercher.
    """
    list_to_be_browsed_through = []
    for i in range(9,-1,-1):
        list_to_be_browsed_through.append(str(i))

    for i in list_to_be_browsed_through:
        try:
            t, reminder = (find_elem(elem, str_to_be_found=f"{i}"))
            if elem != None:
                if reminder > length_next:
                    return i, t
        except TypeError:
            next


def for_one_elem_in_list(test):
    """
    en s'appuyant sur la fonction test_len_and_possibility, celle-ci permet de déterminer
    le plus grand nombre composé de 12 digits pour une suite de caractères donnée.
    """
    biggest_num = []
    length_next=10
    for idx in range(10, -1, -1):
        try:
            i, test = (test_len_and_possibility(test, idx))
            biggest_num.append((i))
            if idx == 0:
                biggest_num.append(str(int(max(test))))
                return biggest_num
        except TypeError:
            for j in range(len(test)):
                i, test = test_len_and_possibility(test, length_next)
                if len(biggest_num) > 11:
                    break
            for i in test:
                biggest_num.append(i)
        length_next = length_next - 1

    return biggest_num


def result_2(text_file = "example_day_3.txt"):
    """
    cette fonction permet de trouver le résultat final attendu dans le challenge, en se basant sur
    toutes celles définies précédemment pour cette partie.
    """
    my_input = open(text_file, "r").read()

    updated_input = my_input.split("\n")[:-1]
    big_nums = []
    for i in range(len(updated_input)):
        test = updated_input[i]
        big_nums.append(int("".join(for_one_elem_in_list(test))))

    return sum(big_nums)

print("Part 2:", result_2("day_3.txt"))
