from locale import currency
from typing import Any


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self) -> str:
        return f"Node{self.value}"


class Doubly_Linked_List():
    def __init__(self) -> None:
        self.head = self.tail = None
        self.length = 0

    def __iter__(self) -> Any:
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self) -> str:
        return "<->".join([str(item) for item in self]) + f" (Head: {self.head}, Tail: {self.tail}, length: {self.length})"

    def push(self, value):
        """
        Insert element from the end

        Args:
            value (int): to insert it in a linked list

        Returns:
            self: return the doubly linked list
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        """ This function should remove a node at the end of the DoublyLinkedList.

        Returns:
            It should return the node removed.
        """
        if not self.head:
            return False
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = popped_node.previous
            self.tail.next = None
            popped_node.previous = None
        self.length -= 1
        return True

    def shift(self):
        """This function should remove a node at the beginning of the DoublyLinkedList.

        Returns:
            It should return the node removed.
        """
        if not self.head:
            return False
        current = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = current.next
            self.head.previous = None
            current.next = None
        self.length -= 1
        return current

    def unshift(self, value):
        """This function should accept a value and add a node to the beginning of

        Args:
            value (any): Value to be added at the begning of linked List

        Returns:
            It should return the DoublyLinkedList.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    def __getitem__(self, index) -> Any:
        """This internal/helper function should find a node at a specified index  in a DoublyLinkedList

        Args:
            index (int): to find node at a particular index

        Returns:
            It should return the found node.
        """
        if index < 0 or index > self.length - 1:
            return None
        current = None
        if index < self.length//2:
            current = self.head
            for i in range(0, index):
                current = current.next
        else:
            current = self.tail
            for i in range(self.length-1, index, -1):
                current = current.previous
        return current

    def __setitem__(self, index, value) -> Any:
        """This function should accept an index and a value and update the value of the node in the DoublyLinkedList at the index with the new value.

        Args:
            index (int): to find node at a particular index
            value (any): Value to be replaced at that node

        Returns:
             It should return true if the node is updated successfully, or false if an invalid index is passed in.
        """
        found_node = self.__getitem__(index)
        if found_node:
            found_node.value = value
            return True
        return False

    def insert(self, index, value):
        """This internal/helper function should insert a node at a specified index in a DoublyLinkedList.

        Args:
            index (int): to find node at a particular index
            value (any): To be inserte node of value at given index

        Returns:
            It should return true if the index is valid and false if the index is invalid (less than 0 or greater than the length of the list).
        """
        if index < 0 or index > self.length - 1:
            return None
        if index == self.length:
            return not not self.push(value)
        if index == 0:
            return not not self.unshift(value)
        new_node = Node(value)
        follow = self.__getitem__(index-1)
        ahead = follow.next
        follow.next = new_node
        new_node.previous = follow
        new_node.next = ahead
        ahead.previous = new_node
        self.length += 1
        return True

    def remove(self, index):
        """This function should remove a node at a specified index in a DoublyLinkedList.

        Args:
            index (int): to find node at a particular index

        Returns:
             It should return the removed node, if the index is valid, or undefined if the index is invalid.
        """
        if index < 0 or index > self.length - 1:
            return None
        if index == self.length:
            return not not self.pop()
        if index == 0:
            return not not self.shift()
        found_node = self.__getitem__(index)
        before_node = found_node.previous
        after_node = found_node.next
        before_node.next = after_node
        after_node.previous = before_node
        self.length -= 1
        return True

    def reverse(self):
        """This function should reverse all of the nodes in a DoublyLinkedList,

        Returns:
            should return the list.
        """
        current = self.head
        while(current):
            current.next, current.previous = current.previous, current.next
            current = current.previous
        self.head, self.tail = self.tail, self.head
        return self


doubly_linked_list = Doubly_Linked_List()
doubly_linked_list.push("hello")
doubly_linked_list.push("Tata")
doubly_linked_list.push("Bye")
doubly_linked_list.push("Bye")
doubly_linked_list.push("GoodBye")
print(doubly_linked_list)
doubly_linked_list.pop()
print(doubly_linked_list)
doubly_linked_list.shift()
print(doubly_linked_list)
doubly_linked_list.unshift("First")
print(doubly_linked_list)
print(doubly_linked_list[1])
doubly_linked_list[3] = "Hello Betta"
print(doubly_linked_list)
doubly_linked_list.insert(3, "Bye")
print(doubly_linked_list)
doubly_linked_list.remove(1)
print(doubly_linked_list)
print(doubly_linked_list.reverse())

# ------------- Big O notation
# Insertion : O(1)
# Removal: O(1)
# Searching: O(n)
# Access: O(n)
