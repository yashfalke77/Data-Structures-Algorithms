# Binary search is much faster form of search
# Rather than eleminating one element at a time , we can eleminate half of the element at atime
# Binary only works on sorted arrays

def binary_search(element, arrs):
    low = 0
    high = len(arrs) - 1
    while(low <= high):
        middle = (low + high) // 2
        if arrs[middle] == element:
            return middle
        else:
            if arrs[middle] < element:
                low = middle + 1
            elif arrs[middle] > element:
                high = middle - 1
    return -1


print(binary_search(element=15, arrs=[
      1, 3, 4, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19]))

print(binary_search(element=25, arrs=[
      1, 3, 4, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19]))

# Best Case: O(1)
# Average Case and Worst Case: O(logn)
