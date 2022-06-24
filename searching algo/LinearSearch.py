# Element are searched in a sequential manner starts from 1st element till the element is found
def linear_search(element, args):
    for i in range(len(args)):
        if args[i] == element:
            return i
    return -1


print(linear_search(10, [34, 26, 10, 5, 37]))
print(linear_search(80, [34, 26, 10, 5, 37]))

# BIG O of Linear Search (Time Complexity)
# Best Case: O(1) (getting the element right away)
# Average Case: O(n)
# Worst Case: O(n) (getting element at last)
