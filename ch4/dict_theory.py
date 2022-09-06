#### DICTS AS HASH TABLES


#### PREREQUISITES

# binary representation
0b101 == 7

# int to binary
bin(7)



##### PROCEDURE

# masking for hash tables: int & binary mask, e.g.:
2576 & 0b111
# Here the size is 0b111 == bin(8 - 1) (8 slots of memory assigned to dict)
# This returns an int
# If the key matches the new key value we are trying to match, then we are all set (return)
# If the space is occupied, then probing must be used to find a new space
# Also, Python stores key/value in standard array, and saves the index of said
# array into the hast table 

# probing
def linear_probing(key, mask=0b111):
    # convert to integer
    perturb = hash(key)
    i = perturb & mask
    yield i
    while True:
        # this equation is from Linear Congruential Generator
        i = (i * 5 + perturb + 1 )
        yield i

# to test
generator = linear_probing("some_key")
next(generator)

# More akin to Python's probing
def sophisticated_probing(key, mask=0b111, PERTURB_SHIFT=5):
    # convert to integer
    perturb = hash(key)
    i = perturb & mask
    yield i
    while True:
        # This shifting avoids collisions
        perturb = perturb >> PERTURB_SHIFT
        i = (i * 5 + perturb + 1 )
        yield i

# 1. Scheme distributes data evenly (load factor, depends on hashing algorithm's entropy)
# 2. Add contribution from higher order values to avoid collision of probed indices


# Dummy idea of how it works
from typing import Union, Callable

class DictWithList:
    """Implementation that uses lists for dealing with hash collisions (not what Python does)."""
    def __init__(self, hash_func: Union[Callable, None] = None, mask: int = 0b111, **kwargs):
        self.data = [[] for i in range(mask)]
        self.hash_func = hash_func or self.ord_hash
        self.mask = mask

        for k, v in kwargs.items():
            masked_key = hash_func(k) & mask
            # data is stored in a list
            self.data[masked_key].append((k, v))
    
    @staticmethod
    def ord_hash(key):
        # This simple hash generator will have lots of collisions
        return ord(key[0])
    
    def lookup(self, key):
        hash_key = self.hash_func(key) & self.mask
        keys_and_values = self.data[hash_key]
        for k_v in keys_and_values:
            if k_v[0] == key:
                return k_v[1]
        
        raise KeyError("Inexistent key")
    
    def insert(self, key, value):
        """Inserts into keys which have a list (probing would be used instead)."""
        hash_key = self.hash_func(key) & self.mask
        keys_and_values = self.data[hash_key]
        
        if keys_and_values is not None:
            print(f"Hash collision: key space taken by {keys_and_values}.")
        
        for i, k_v in enumerate(keys_and_values):
            if key == k_v[0]:
                print(f"Replacing key: {k_v}")
                self.data[hash_key][i] = (key, value)
                return
        
        self.data[hash_key].append((key, value))
    
    def delete(self, key):
        hash_key = self.hash_func(key) & self.mask
        keys_and_values = self.data[hash_key]
        for i, k_v in enumerate(keys_and_values):
            if key == k_v[0]:
                self.data[hash_key] = self.data[hash_key][i + 1:]
                return
        raise KeyError(f"Key does not exist.")


### RESIZING

# Python will resize a dict once it has 2/3 of its capacity full, by multiplying by 3X this 2/3 size:
# starting with 8 (2/3 = 6), 18 (3*6, 2/3 = 13), 39, 81, etc

# When resizing:
# 1. A larger table is allocated
# 2. Mask is adjusted to fit the new table 
# 3. All elements of older table are allocated into new table.

# This is a slower operation then just inserting. Still, amortized cost is O(1).
# Resizing can increase or decrease dict size, but it only happens during inserts.    


### IMPORTING MODULES

# Python looks for variables in: (1) locals(); (2) globals(); (3) __builtins__;
# globals() and __builtins__ imply a dictionary lookup, which can sometimes be simplified by declaring the variable once.


