# A method for solving complex problem by breaking down it into  collection of simpler subproblems, solving each of those subproblems just once and storing their solutions
# For Dynamic Programming we need RECURSION

# ! IT ONLY WORKS ON PROBLEMS WITH
# ! 1) OPTIMAL SUBSTRUCTURE
# ! 2) OVERLAPPING SUBPROBLEMS

# ------------------------------------------------ OVERLAPPING SUBPROBLEMS -------------------------------------------------
# A  Problem is said to have Overlapping Subproblems it can be broken down into subproblems which are reused several times

# Eg: In Febonnaic Series - Every number after the first two is the sum of the two preceding ones (Overlapping subproblems)

# ------------------------------------------------ OPTIMAL SUBSTRUCTURE -------------------------------------------------
# A problem is said to have optimal substructure if an optimal solution can be constructed from optimal solutions of its subproblems

# TODO (Problem Statement): Caluculate N th digit in febonnaci series

# Without using Dynamic Programming
# Time Complexity: O(2**n) [Worst than O(n*n)]

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(4))

# ------------------------------------- MEMOIZATION ------------------------------------------------
# Storig the results of expensive functions  calls and returning the cached result if same input occur again
# Follows Top Down Approach
# Time Complexity: O(n)


def fib1(n, memo={"1": 1, "2": 2}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    res = fib1(n-1, memo) + fib1(n-2, memo)
    memo[n] = res
    return res


print(fib1(50))

# -------------------------------- Tabulation -------------------------------------------------------
# Storing the result of previous result in a "table" (usually an array)
# Usually done using iteration
# Better space complexity can be achieved using tabulation
# Follows Bottom top Approach
# Time Complexity: O(n)


def fib2(n):
    if n <= 2:
        return 1
    fib_nums = [None]*(n+1)
    fib_nums[1] = 1
    fib_nums[2] = 1
    for i in range(3, n + 1):
        fib_nums[i] = fib_nums[i-1] + fib_nums[i-2]
    return fib_nums[n]


print(fib2(50))
