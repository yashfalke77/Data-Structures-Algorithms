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
# Time Complexity: O(2**n)

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(4))
