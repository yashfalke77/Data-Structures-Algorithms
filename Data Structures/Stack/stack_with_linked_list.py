from tkinter.messagebox import NO
from typing import Any


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f"Node{self.value}"


class Stack:
    def __init__(self) -> None:
        self.first = self.last = None
        self.size = 0

    def __iter__(self) -> Any:
        node = self.first
        while node:
            yield node.value
            node = node.next

    def __str__(self) -> str:
        return "->".join([str(item) for item in self]) + f" (First: {self.first}, Last: {self.last}, size: {self.size})"

    def push(self, value):
        """Takes in a node and puts it at the top of the stack.

        Args:
            value (int): Value to be inserted at the top of stack

        Returns:
            Should return the new size of the stack.
        """
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            old_first = self.first
            self.first = new_node
            new_node.next = old_first
        self.size += 1
        return self.size

    def pop(self):
        """Removes the node at the top of the stack

        Returns:
            returns the value of that node.
        """
        if not self.first:
            return False
        if self.first == self.last:
            self.last = None
        current = self.first
        self.first = current.next
        current.next = None
        self.size -= 1
        return current


stack = Stack()
stack.push("Hello")
stack.push("bettaa")
print(stack)
stack.pop()
stack.pop()
print(stack)
