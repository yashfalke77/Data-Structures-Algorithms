def naive_string_search(pattern, string):
    count = 0
    for i in range(len(string)):
        for j in range(len(pattern)):
            if pattern[j] != string[i+j]:
                break
            if j == len(pattern)-1:
                count += 1
    return count


print(naive_string_search(pattern="lo", string="lorie loled"))

# Best Case: O(n) (When the first letter does not match with any letter in the stinrg hence only one outer loop runs)
# Worst Case: O((n-m+1)*m) (where all character of pattern and string is same or only end character of string is different)
