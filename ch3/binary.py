import bisect
from copy import deepcopy

from data import list_long, list_short


# Binary search implementation
def binary_search(ord_list, search_value):
    def _binary_search(ord_list, search_value, i, j):
        while i < j:
            mid_ind = int((j - i) / 2) + i
            mid_val = ord_list[mid_ind] 
            if mid_val == search_value:
                return mid_ind
            if mid_val < search_value:
                return _binary_search(ord_list, search_value, mid_ind + 1, j)
            return _binary_search(ord_list, search_value, i, mid_ind)
        return -1
    return _binary_search(ord_list, search_value, 0, len(ord_list))


if __name__ == "__main__":
    # Bisect module
    print("List before insertions")
    print(list_long[:5], "\n")
    # Where should value be inserted to keep the list in order?
    value = 3
    insert_index = bisect.bisect(list_long, value)
    list_long.insert(insert_index, value)
    print(f"Inserted {value}")
    print(list_long[:5], "\n")

    # You can also do it all together with bisect.insort
    value = 4
    bisect.insort(list_long, value)
    print(f"Inserted {value}")
    print(list_long[:5], "\n")

    listas = [list_short, list_long]
    for lista in listas:
        for val in lista:
            implemented = binary_search(lista, val)
            built_in = lista.index(val)
            bisect_value = bisect.bisect(lista, val)
            message = f"Value: {val}. Implemented: {implemented}. Built in: {built_in}. Bisect minus 1: {bisect_value - 1}"
            print(message)
            assert implemented == built_in == bisect_value - 1, message
    

