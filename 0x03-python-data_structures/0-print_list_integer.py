#!/usr/bin/python3
def print_list_integer(_list=[]):
    for i in _list:
        print('{:d}'.format(i))

vi 1-element_at.py

#!/usr/bin/python3
def element_at(my_list, idx):
    return(my_list[idx] if 0 <= idx < len(my_list) else "None")

vi 2-replace_in_list.py

#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return(my_list)

vi 3-print_reversed_list_integer.py

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in reversed(my_list):
        print('{:d}'.format(i))

vi 4-new_in_list.py

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp_list = my_list[:]
    if 0 <= idx < len(my_list):
        tmp_list[idx] = element
        return(tmp_list)
    return(my_list)

vi 5-no_c.py

#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for i in my_string:
        if (i != 'c') and (i != 'C'):
            new_str += i
    return (new_str)

vi 6-print_matrix_integer.py

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print(' '.join('{:d}'.format(j)for j in i))
