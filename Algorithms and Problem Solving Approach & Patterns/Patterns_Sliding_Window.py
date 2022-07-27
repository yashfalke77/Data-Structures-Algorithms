#  This type of approach is used when we have to find sub array or sub string from arrays or string
# This pattern involves creating a window which can either be an array or number from one position to another
# Depending on a certain condition, the window either increases or closes (and a new window is created)
# Very useful for keeping track of a subset of data in an array/string etc

# TODO (problem statement): Write a function called maxSubarraySum which accepts an array of integers and a number called n. The function should calculate the maximum sum of n consecutive elements in the array.

import math

# without using sliding window
# Time Complexity: O(n*n)


def maxSubarraySum(arr: list, num: int):
    if num > len(arr):
        return None
    max_num = -math.inf
    for i in range(0, len(arr) - num):
        sum = 0
        for j in range(0, num+1):
            sum += arr[i+j]
        max_num = max(max_num, sum)
    return max_num


print(maxSubarraySum([1, 2, 5, 2, 8, 1, 5], 2))
print(maxSubarraySum([1, 2, 5, 2, 8, 1, 5], 4))
print(maxSubarraySum([4, 2, 1, 6], 1))
print(maxSubarraySum([4, 2, 1, 6, 2], 4))
print(maxSubarraySum([], 4))


# using sliding window
# Time Coplexity: O()
def maxSubarraySum1(arr: list, num: int):
    if num > len(arr):
        return None
    temp_sum = 0
    max_sum = 0
    for i in range(0, num):
        max_sum += arr[i]
    temp_sum = max_sum
    for i in range(num, len(arr)):
        temp_sum = temp_sum - arr[i-num] + arr[i]
        max_sum = max(temp_sum, max_sum)
    return max_sum


print("-----------")

print(maxSubarraySum1([1, 2, 5, 2, 8, 1, 5], 2))
print(maxSubarraySum1([1, 2, 5, 2, 8, 1, 5], 4))
print(maxSubarraySum1([4, 2, 1, 6], 1))
print(maxSubarraySum1([4, 2, 1, 6, 2], 4))
print(maxSubarraySum1([], 4))
