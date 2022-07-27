# Some Patterns:
# Frequency Counter
# Multiple Pointers
# Sliding Window
# Divide and Conquer
# Dynamic Programming
# Greedy Algorithms
# Backtracking

# --------------------------- 1) Frequency Counter ----------------------------------------
# * This pattern uses objects or sets to collect values/frequencies of values
# * This can often avoid the need for nested loops or O(N^2) operations with arrays / strings

# ? The Frequency Counter pattern is most helpful when you have multiple pieces of data that you want to compare with one another.

# TODO (Problem Statement): Write a function called same, which accepts two arrays. The function should return true if every value in the array has it's corresponding value squared in the second array. The frequency of values must be the same.
# Without using Frequency Counter
# Time Complexity: O(n**2)
def same(arr1: list, arr2: list):
    if len(arr1) != len(arr2):
        return False
    for element in arr1:
        if element ** 2 not in arr2:
            return False
        correct_index = arr2.index(element**2)
        arr2.pop(correct_index)
    return True


# print(same([1, 2, 1], [4, 4, 1]))

# Using Frequency Counter
# Time Complexity: O(n)


def same1(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    frequency_counter1 = {}
    frequency_counter2 = {}
    for element in arr1:
        if not element in frequency_counter1:
            frequency_counter1[element] = 1
        else:
            frequency_counter1[element] += 1
    for element in arr2:
        if not element in frequency_counter2:
            frequency_counter2[element] = 1
        else:
            frequency_counter2[element] += 1
    for key in frequency_counter1:
        if not (key ** 2 in frequency_counter2):
            return False
        if frequency_counter1[key] != frequency_counter2[key**2]:
            return False
    return True


# print(same1([1, 2, 1], [4, 4, 1]))

# TODO (Problem Statement): Given two strings, write a function to determine if the second string is an anagram of the first. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman


def anagram(word1: str, word2: str):
    frequency_counter1 = {}
    frequency_counter2 = {}
    for char in word1.lower():
        if char in frequency_counter1:
            frequency_counter1[char] += 1
        else:
            frequency_counter1[char] = 1
    for char in word2.lower():
        if char in frequency_counter2:
            frequency_counter2[char] += 1
        else:
            frequency_counter2[char] = 1
    for key in frequency_counter1:
        if key not in frequency_counter2:
            return False
        if frequency_counter1[key] != frequency_counter2[key]:
            return False
    return True


def valid_anagram(word1: str, word2: str):
    if len(word1) != len(word2):
        return False
    lookup = {}
    for char in word1.lower():
        if char in lookup:
            lookup[char] += 1
        else:
            lookup[char] = 1
    for char in word2:
        if char not in lookup or lookup[char] <= 0:
            return False
        else:
            lookup[char] -= 1
    return True


print(valid_anagram('', ''))
print(valid_anagram('aaz', 'zza'))
print(valid_anagram('anagram', 'nagaram'))
print(valid_anagram("rat", "car"))
print(valid_anagram('awesome', 'awesom'))
print(valid_anagram('qwerty', 'qeywrt'))
print(valid_anagram('texttwisttime', 'timetwisttext'))
