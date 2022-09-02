# Let us consider the following problem to understand Binary Indexed Tree.
# We have an array arr[0 . . . n-1]. We would like to
# 1 Compute the sum of the first i elements.
# 2 Modify the value of a specified element of the array arr[i] = x where 0 <= i <= n-1.
# A simple solution is to run a loop from 0 to i-1 and calculate the sum of the elements. To update a value, simply do arr[i] = x. The first operation takes O(n) time and the second operation takes O(1) time. Another simple solution is to create an extra array and store the sum of the first i-th elements at the i-th index in this new array. The sum of a given range can now be calculated in O(1) time, but the update operation takes O(n) time now. This works well if there are a large number of query operations but a very few number of update operations.

# ----------------------------------------------- Fenwick tree -----------------------------------------------
# Fenwick trees lenght is +1 more time than the given array
# Fenwick trees each index can be calculated as Follows:
# 1) convert index into binary
# 2) convert right most set bit  (1 bit) to zero
# 3) convert it into decimal and add it with 1
# The value of that index represent sum of that range

# Fenwick Tree updation can be done as follows:
# 1) take index from array and add its value to the same index of fenwick tree
# 2) To finde next index , first do 2's complement on index
# 3) and it with binary of original
# 4) add it with original number
# 5) convert final binary number into decimal that is next integer


# To find any given sum range
#  1) first do 2's complement on index
# 2) and it with binary of original
# 3) subtract with original number it with original number

class BIT:
    def __init__(self, nums: list[int]):
        self.nums = [0]*(len(nums) + 1)
        self.length = len(self.nums)

    def update(self, index: int, value: int):
        j = index + 1
        while j < self.length:
            self.nums[j] += value
            j += (j & -j)

    def query(self, index: int):
        sum = 0
        j = index + 1
        while j > 0:
            sum += self.nums[j]
            j -= (j & -j)


class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.bit = BIT(nums)
        for index, value in enumerate(nums):
            self.bit.update(index, value)

    def update(self, index: int, val: int) -> None:
        value = val - self.nums[index]
        self.bit.update(index, value)
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query(right) - self.bit.query(left - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
