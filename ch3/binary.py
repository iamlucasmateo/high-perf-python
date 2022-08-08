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
    list_1 = [1,2,3,4,5,6,7,8]
    list_2 = [1,5,9,12,15,17,20,24,27,29,35,37,40, 42,48,57,78,83,94,102,139,157,177,233,245,367]
    listas = [list_1, list_2]
    for lista in listas:
        for val in lista:
            implemented = binary_search(lista, val)
            built_in = lista.index(val)
            message = f"Value: {val}. Implemented: {implemented}. Built in: {built_in}"
            print(message)
            assert binary_search(lista, val) == lista.index(val), message
    

