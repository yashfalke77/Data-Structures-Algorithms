# Ann sorting algorithm where largest value bubble up to top
def swap(arr, indx1, indx2):
    [arr[indx1], arr[indx2]] = [arr[indx2], arr[indx1]]


def bubble_sort(arr):
    for i in range(len(arr), 0, -1):
        noSwaps = True
        for j in range(0, i-1):
            print(arr, arr[j], arr[j+1], i, j)
            if arr[j] > arr[j+1]:
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]]
                noSwaps = False
        if noSwaps:
            break
    return arr


print(bubble_sort(arr=[5, 3, 4, 1, 2]))
print("-----------------------------")
print(bubble_sort(arr=[5, 1, 2, 3, 4]))

# Time Complexity
# Worst case/ Average Case: O(n*n)
# Best Case: O(n) (Most of the elements are already in a sorted order)
# Space Complexity: O(1)
