# Hash Tables are used to store key value pairs
# They are like arrays/ lists but keys are not ordered

# ------------------------------ Implementation ---------------------------------------
# To implement hash table we will be using an array
# Inorder to look values by key we need to convert key into valid array indices
# A function that performs this taskis called hash function
# A hash function is function who takes input of any size and gives output of fixed size\
# A Good Hash Function should be fast , distribute keys uniformly and be deterministic
from typing import Any


class Hash_Table:
    def __init__(self, size=4) -> None:
        self.key_map = [None] * size

    def __repr__(self) -> str:
        return f"{self.key_map}"

    def hash(self, key: str):
        total = 0
        weird_prime = 31
        final = min(len(key), 100)
        for i in range(0, final):
            value = ord(key[i]) - 96
            total = (total * weird_prime + value) % len(self.key_map)
        return total

    def set(self, key: str, value: Any):
        index = self.hash(key)
        if self.key_map[index] == None:
            self.key_map[index] = []
        self.key_map[index].append([key, value])

    def get(self, key: str):
        index = self.hash(key)
        if self.key_map[index] != None:
            for pairs in self.key_map[index]:
                if pairs[0] == key:
                    return pairs[1]
        return None

    def keys(self):
        key_array = []
        for array in self.key_map:
            if array == None:
                continue
            for pairs in array:
                if pairs[0] not in key_array:
                    key_array.append(pairs[0])
        return key_array

    def values(self):
        key_array = []
        for array in self.key_map:
            if array == None:
                continue
            for pairs in array:
                if pairs[1] not in key_array:
                    key_array.append(pairs[1])
        return key_array


ht = Hash_Table(17)
ht.set("maroon", "#800000")
ht.set("yellow", "#FFFF00")
ht.set("olive", "#808000")
ht.set("salmon", "#FA8072")
ht.set("lightcoral", "#F08080")
ht.set("mediumvioletred", "#C71585")
ht.set("plum", "#DDA0DD")
ht.set("mediumvioletred", "#C70582")
print(ht)
print(ht.get("maroon"))
print(ht.keys())
print(ht.values())

# Collosion : If there are more than 1 element having same address then it is called as collosion
# Collosion handling Technique:
#  1) Separate Chaining: at each index in our array we store values using a more sophosticated data structure (array or linked list)
# 2) Linear probing: When we find a collosion we search through the array to fing next empty slot

# ----------------------------------------------- Big O Complexity -------------------------------------------------------
# A good has function will give this time complexity with have constant of Big O
# Insert (Average Case): O(1)
# Deletion (Average Case): O(1)
# Access (Average Case): O(1)
