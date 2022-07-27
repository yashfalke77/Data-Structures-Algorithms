# ----------------------------------- 2) Multiple Pointer -------------------------------------------
# * Creating pointers or values that correspond to an index or position and move towards the beginning, end or middle based on a certain condition
# * Very efficient for solving problems with minimal space complexity as well

# TODO (Problem Statement): Write a function called sumZero which accepts a sorted array of integers. The function should find the first pair where the sum is 0. Return an array that includes both values that sum to zero or undefined if a pair does not exist

# Without using multiple pointers
# Time Complexity: O(n*n)

def sum_zero(arr: list):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == 0:
                return [arr[i], arr[j]]


print(sum_zero([-4, -3, -2, -1, 0, 1, 2, 5]))

# using Multiple Pointers
# Time Complexity: O(n)


def sum_zero1(arr: list):
    left = 0
    right = len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == 0:
            return [arr[left], arr[right]]
        elif sum > 0:
            right -= 1
        else:
            left += 1


print(sum_zero1([-4, -3, -2, -1, 0, 1, 2, 5]))

# TODO (problem statement): Implement a function called countUniqueValues, which accepts a sorted array, and counts the unique values in the array. There can be negative numbers in the array, but it will always be sorted.


def count_unique_value(arr: list):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return arr[:i+1]


print(count_unique_value([1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 7]))
