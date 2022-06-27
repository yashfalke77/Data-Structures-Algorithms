def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i-1
        while(j >= 0 and arr[j] > current_value):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current_value
    return arr


print(insertion_sort(arr=[2, 1, 9, 76, 4]))

# Time Complexity:  O(n*n) (Worst Case)
# O(n) (Best Case)
# Space Complexity: O(1)
