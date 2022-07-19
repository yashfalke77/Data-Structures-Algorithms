# for implementation of binary heap we use List / Array
# 1) for any index of an array n
# Left child is stored at 2n +1
# Right child is stored at 2n+2
# 2) from child to root
# Its parent is at index (n-1)/2

import math


class Max_Binary_Heap:
    def __init__(self) -> None:
        self.values = []

    def __repr__(self) -> str:
        return f"{self.values}"

    def insert(self, value):
        self.values.append(value)

        def bubble_up():
            index = len(self.values) - 1
            while index > 0:
                parent_index = math.floor((index - 1) / 2)
                if self.values[index] < self.values[parent_index]:
                    break
                self.values[index], self.values[parent_index] = self.values[parent_index], self.values[index]
                index = parent_index

        bubble_up()

    def extract_max(self):
        removed_element = None
        if len(self.values) > 0:
            self.values[0], self.values[len(
                self.values) - 1] = self.values[len(self.values) - 1], self.values[0]
            removed_element = self.values.pop()

        def bubble_up():
            parent_index = 0
            while True:
                left_child_index = 2*parent_index + 1
                right_child_index = 2*parent_index + 2
                left_child = None
                right_child = None
                swap = None

                if left_child_index < len(self.values) - 1:
                    left_child = self.values[left_child_index]
                    if left_child > self.values[parent_index]:
                        swap = left_child_index
                if right_child_index < len(self.values) - 1:
                    right_child = self.values[right_child_index]
                    if (swap == None and left_child_index < len(self.values) - 1) or (swap != None and right_child > left_child):
                        swap = right_child_index
                if swap == None:
                    break
                self.values[parent_index], self.values[swap] = self.values[swap], self.values[parent_index]
                parent_index = swap

        bubble_up()
        return removed_element


# removing is remove max element in max_heap and min element in min_heap
heap = Max_Binary_Heap()
heap.insert(55)
heap.insert(39)
heap.insert(41)
heap.insert(18)
heap.insert(27)
heap.insert(12)
heap.insert(33)
print(heap)
heap.extract_max()
print(heap)


# -------------------------------------- Big O of Binar Heap (Time Complexity) --------------------------
# 1)  Insertion, Removal: O(logn)
# Each time going a step down level in binary heap we have two times no of node
# For worst case inserting the max element in Max binary heap , we have to compare one time per level of binary heap
# worst case of binary search tree is removed by binary heap as in heap we have to fill all node in one level then move to next level , so leftsided binary tree or right sided binary tree is not possible

# 2) search : O(n)
# as like binary tree we dont have left side greater than right side hence we have check all the nodes (considering worst case)
