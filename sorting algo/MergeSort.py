# Follows divide and conquer strategy
# Divide: elements are divided into parrtitions
# conquer: Element from each partition will be sorted
# combine: solution of each partition will be combined to get final solution


from math import floor


def merge(arr1, arr2):
    i = 0
    j = 0
    sorted_array = []
    while(i < len(arr1) and j < len(arr2)):
        if arr1[i] < arr2[j]:
            sorted_array.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            sorted_array.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_array.append(arr2[j])
        j += 1
    return sorted_array


# print(merge([1, 10, 50], [2, 14, 99, 100]))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = floor(len(arr)/2)
    left = merge_sort(arr[: mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


print(merge_sort([10, 24, 76, 73, 72, 1, 9]))

# Time Complexity: O(nlogn) (For all cases)
# why logn because for dividing the array requires logn times into single element array
# if 32 element is present in arrray then 2^5 i.e 5 pases are required to divide it into single elements araays
# after decomposition we are doing array length (n) comparisions and then merging for sorting
# Hence Time Complexity: O (nlogn)

# Space Complexity: O(n)
