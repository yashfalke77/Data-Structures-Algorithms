# problem statement : create a function gives sum from 1 upto n which given through input
# Counting: count the no of operations has to perform
# Method 1
# Here 1 assignment and n addition,n assignment and n addition , nassignment
# So total 4n +2 is counting, it increases as input increases
# Complexity is O(n)
def addUpTo(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


# Method 2
# Here counting is 3 operations which are independent of n
# Complexity is O(1)
def addUpTo1(n):
    return n * (n+1)/2


# Hence Method 2 is more faster than method 1
print(addUpTo(6))
print(addUpTo1(6))

# Which method is better?
# method is better means it is Faster, Less memory intensive and more readable
# more focus is on Faster and Less Memory Intensive

# -------------------------------------- Big O Notation ------------------------
# Big O notation is a way to formalize counting
# It allow us formally to talk about how runtime of algorithm grow as input grow
# It is given by O(f(n))
# 1) f(n) could be linear (f(n) = n)
# 2) f(n) could be quadratic (f(n) = n^2)
# 1) f(n) could be constant (f(n) = 1)
# 1) f(n) could be Entirely different


def countUpAndDown(n):
    print("Going up")
    for i in range(n):
        print(i)
    print("At the Top!\nGoing Down ")
    for j in range(n-1, 0, -1):
        print(j)


# here , as n grows we have n operations for 1 foor loop
# for other n for 2nd for loop , Hence n+n=2n
# For bigger picture  Big O Notation is O(n)
countUpAndDown(n=10)


def printAllPairs(n):
    for i in range(n):
        for j in range(n-1, 0, -1):
            print(i, j)


# Here O(n) for outer loop and O(n) for inner Loop hence
# Total is : O(n^2)
printAllPairs(10)

# -------------------------- Simplifying Big O Operations -----------------------------
# 1) CONSTANTS DOES NOT MATTER
# eg: O(2n) = O(n), O(500)=O(1), O(2n^2)=O(n^2)
# 2) SMALL TERMS DOES NOT MATTER
# eg: O(n^2+5n+8) = O(n^2), O(n+2) = O(n)

# THESE ARE TIME COMPLEXITY

# --------------------------- SPACE COMPLEXITY---------------------------------------
# We do not include the space taken up by the input
# Most primitives are constat spaces(boolean, number, undefined and null)
# String require O(n) space (Where n is the length of string)
# Arrays and objects (Reference type) require O(n) space (Where n is the length of refernce types)

# ---------------------------- Logarithms in Big O notation -------------------------
# here log base 2 into n is equal to log n
# -- BEST to WORST big(O):  O(1) , O(logn), O(n), O(nlogn), O(n*n)

# ------------------------------- Dictionaries with Big O notation (space complexity)-----------------------
# insertion , removal , Access is O(1)
# searching is O(n)

# -------------------------- List in Big O notation (space complexity) --------------------------------
# searching is O(n)
# Access is O(1)
# insertion : at end (O(1)) and at start (O(N)) (because we have reorder the index so its visit evry element)
# removal : at end (O(1)) and at start (O(N)) (because we have reorder the index so its visit evry element)
