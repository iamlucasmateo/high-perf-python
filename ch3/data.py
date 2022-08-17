import random
from copy import deepcopy
import typing


list_short = [1,2,3,4,5,6,7,8]
list_long = [1,5,9,12,15,17,20,24,27,29,35,37,40,42,48,57,78,83,94,102,139,157,177,233,245,367]

def shuffle_list(array: typing.Iterable):
    return random.shuffle(array)

# Sorting
def sort_func(x):
    # transformation to be applied to element before sorting (key)
    return x % 3

if __name__ == "__main__":
    list_sorted_1 = sorted(list_long)
    print(list_sorted_1)
    list_sorted_2 = sorted(list_long, key=sort_func)
    print(list_sorted_2)
    
    list_sorted_3 = deepcopy(list_long)
    # in place (reeturns None), slightly more efficient; can also take in "key"
    list_sorted_3.sort()

