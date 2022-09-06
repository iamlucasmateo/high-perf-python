import string
import timeit

### HASH FUNCTIONS

# We'd want the hash functions to distribute keys as uniformly as possible (entropy of a hash function)
# This will depend on the nature of the keys.

class BadHash(str):
    def __hash__(self):
        return 42

class GoodHash(str):
    def __hash__(self):
        """Hash optimized for two character words."""
        return ord(self[1]) + 26 * ord(self[0]) - 2619


bad_set = set()
good_set = set()

for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        key = i + j
        bad_set.add(BadHash(key))
        good_set.add(GoodHash(key))
    
    
    
bad_time = timeit.repeat(
    "key in bad_set",
    setup = "from __main__ import bad_set, BadHash; key = BadHash('zz')",
    repeat = 3,
    number = 1_000_000
)

good_time = timeit.repeat(
    "key in good_set",
    setup = "from __main__ import good_set, GoodHash; key = GoodHash('zz')",
    repeat = 3,
    number = 1_000_000
)

print(f"Min lookup in bad_set: {min(bad_time)}")
print(f"Min lookup in good_set: {min(good_time)}")
