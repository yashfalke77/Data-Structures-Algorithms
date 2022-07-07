# A data structure that contains a head, tail adn length property
# A linked list consists of nodes and each nodes has a value and pointer to another node or null

from typing import Any


class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"Node{self.value}"


class Singly_Linked_List():
    def __init__(self) -> None:
        self.head = self.tail = None
        self.length = 0

    def __iter__(self) -> Any:
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __str__(self) -> str:
        return "->".join([str(item) for item in self]) + f" (Head: {self.head}, Tail: {self.tail}, length: {self.length})"

    def push(self, value):
        """
        Insert element from the end
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        """
        Remove the element from the end
        """
        if not self.head:
            return "Node not found"
        else:
            current = self.head
            previous = current
            while(current.next):
                previous = current
                current = current.next
            self.tail = previous
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return current

    def shift(self):
        """
        Remove the element from the start
        """
        if not self.head:
            return "Node not found"
        else:
            current = self.head
            self.head = current.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return current

    def unshift(self, value):
        """
        Insert a new Node at the begining of the linked list
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    def __getitem__(self, index) -> Any:
        """
        Indexing Support. Used to get a node at particular position
        """
        if index < 0 or index > self.length - 1:
            return None
        else:
            current = self.head
            counter = 0
            while counter != index:
                current = current.next
                counter += 1
            return current

    def __setitem__(self, index, value) -> None:
        """
        Used to change the data of a particular node
        """
        found_node = self.__getitem__(index)
        if found_node:
            found_node.value = value
            return True
        return False

    def insert(self, index, value):
        """
        Insert data at given index.
        """
        if index < 0 or index > self.length:
            return False
        if index == self.length:
            return not not self.push(value)
        if index == 0:
            return not not self.unshift(value)
        new_node = Node(value)
        previous = self.__getitem__(index - 1)
        current = previous.next
        previous.next = new_node
        new_node.next = current
        self.length += 1
        return True

    def remove(self, index):
        """
        Delete node at given index
        """
        if index < 0 or index > self.length - 1:
            return False
        if index == 0:
            return not not self.shift()
        if index == self.length - 1:
            return not not self.pop()
        previous = self.__getitem__(index-1)
        previous.next = previous.next.next
        return True

    def reverse(self):
        """
        This reverses the linked list order.
        """
        node = self.head
        self.head = self.tail
        self.tail = node
        previous = next = None
        for i in range(0, self.length):
            next = node.next
            node.next = previous
            previous = node
            node = next
        return self


linked_list = Singly_Linked_List()
linked_list.push("Hello")
linked_list.push("Tata")
linked_list.push("Bye")
linked_list.push("Bye")
linked_list.push("GoodBye")
print(linked_list)
linked_list.pop()
print(linked_list)
linked_list.shift()
print(linked_list)
linked_list.unshift("Hello")
print(linked_list)
print(linked_list[3])
linked_list[3] = "hiii"
print(linked_list)
print(linked_list[4])
print(linked_list.insert(5, "First"))
print(linked_list)
print(linked_list.remove(8))
print(linked_list)
print(linked_list.reverse())

# Big O of Singly Linked Lists
# Insertion O(1) (for unshift and push)
# Removal It depends O(1) (for shift) ... or  O(n) (for pop)
# Searching O(n)
# Access O(n)
