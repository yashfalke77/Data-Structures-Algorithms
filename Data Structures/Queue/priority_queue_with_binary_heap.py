# A data structure which has a priority
# Element having high priority is served first as compared to lower priority
# insertion and removal of priority queue using binary heap is O(logn) and using lists and array would be O(n)

# using min binary heap
import math


class Node:
    def __init__(self, value, priority) -> None:
        self.value = value
        self.priority = priority

    def __repr__(self) -> str:
        return f"Node {self.value}"


class Priority_Queue:
    def __init__(self) -> None:
        self.values = []

    def __repr__(self) -> str:
        return f"{self.values}"

    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        self.values.append(new_node)

        def bubble_up():
            index = len(self.values) - 1
            while index > 0:
                parent_index = math.floor((index - 1) / 2)
                if self.values[index].priority > self.values[parent_index].priority:
                    break
                self.values[index], self.values[parent_index] = self.values[parent_index], self.values[index]
                index = parent_index
        bubble_up()

    def dequeue(self):
        removed_element = None
        if len(self.values) > 0:
            self.values[0], self.values[len(
                self.values) - 1] = self.values[len(self.values) - 1], self.values[0]
            removed_element = self.values.pop()

        def bubble_down():
            parent_index = 0
            while True:
                left_child_index = 2*parent_index + 1
                right_child_index = 2*parent_index + 2
                swap = None
                if left_child_index < len(self.values) - 1:
                    left_child = self.values[left_child_index]
                    if left_child.priority < self.values[parent_index].priority:
                        swap = left_child_index
                if right_child_index < len(self.values) - 1:
                    right_child = self.values[right_child_index]
                    if (swap == None and right_child.priority > self.values[parent_index].priority) or (swap != None and left_child.priority > right_child.priority):
                        swap = right_child_index
                if swap == None:
                    break
                self.values[parent_index], self.values[swap] = self.values[swap], self.values[parent_index]
                parent_index = swap

        bubble_down()
        return removed_element


hospital = Priority_Queue()
hospital.enqueue("common cold", 5)
hospital.enqueue("gunshot wound", 1)
hospital.enqueue("high fever", 4)
hospital.enqueue("broken arm", 2)
hospital.enqueue("glass in foot", 3)
print(hospital)

print(hospital.dequeue())
print(hospital.dequeue())
print(hospital.dequeue())
