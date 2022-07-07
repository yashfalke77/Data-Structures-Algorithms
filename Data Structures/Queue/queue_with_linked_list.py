from typing import Any

# Just like linked list but add to the end remove from the begning


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return f"Node{self.value}"


class Queue:
    def __init__(self) -> None:
        self.size = 0
        self.first = self.last = None

    def __iter__(self) -> Any:
        node = self.first
        while(node):
            yield node.value
            node = node.next

    def __str__(self) -> str:
        return "->".join([str(item) for item in self]) + f" (First: {self.first}, Last: {self.last}, size: {self.size})"

    def push(self, value):
        new_node = Node(value)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1
        return self

    def pop(self):
        if not self.first:
            return False
        if self.first == self.last:
            self.last = None
        old_first = self.first
        self.first = old_first.next
        old_first.next = None
        self.size -= 1
        return True


queue = Queue()
queue.push("hello betaa")
queue.push("tata")
print(queue)
queue.pop()
queue.pop()
print(queue)
