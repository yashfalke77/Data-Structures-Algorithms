# A process / function that calls itself

#  Call Stack: Any time a function is invoked it is placed (pushed) on call stack
# When the function end then it is poped from the call stack

# ------------------- working of recursive functions --------------------------------
# Invoke same function with differnt input until youreach your base case
# Base Case: The Condition where recursion ends

# Two essential part of recursive function:
# 1) Base Case
# 2) Different input

# TODO (Problem statement):  Count down

def count_down(num):
    if num <= 0:
        print("All Done")
        return
    print(num)
    num -= 1
    count_down(num)


count_down(5)

# TODO (problem statement): Sum Range of all number upto n


def sum_range(num):
    if num == 1:
        return 1
    if num == 0:
        return 0
    return num + sum_range(num-1)


print(sum_range(3))

# TODO (problem statement): factorial of a number


def factorial(num):
    if num == 1:
        return 1
    return num*factorial(num-1)


print(factorial(5))

# ------------------------------- Helper Method Recursion -----------------------------------


def collect_odds(arr):
    results = []

    def helper(helperInput):
        if len(helperInput) == 0:
            return
        if helperInput[0] % 2 != 0:
            results.append(helperInput[0])
        helperInput.pop(0)
        helper(helperInput)
    helper(arr)
    return results


print(collect_odds([1, 2, 3, 4, 5, 6]))
