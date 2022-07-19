from operator import le
from platform import node
from typing import Any


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = self.right = None

    def __repr__(self) -> str:
        return f"Node{self.value}"


class Binary_Search_Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return self
        else:
            current = self.root
            while(True):
                if value == current.value:
                    return None
                if value < current.value:
                    if current.left == None:
                        current.left = new_node
                        return self
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right == None:
                        current.right = new_node
                        return self
                    else:
                        current = current.right

    def search(self, value):
        if not self.root:
            return False
        else:
            current = self.root
            node_found = False
            while current and not node_found:
                if value < current.value:
                    current = current.left
                elif value > current.value:
                    current = current.right
                else:
                    node_found = True
            if not node_found:
                return False
            return current

    def breadth_first_search(self):
        node = self.root
        queue = []
        data = []
        queue.append(node)
        while len(queue):
            node = queue.pop(0)
            data.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return data

    def depth_first_search_preOreder(self):
        data = []

        def traverse(node):
            data.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return data

    def depth_first_search_postOreder(self):
        data = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            data.append(node.value)
        traverse(self.root)
        return data

    def depth_first_search_inOrder(self):
        data = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            data.append(node.value)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return data


tree = Binary_Search_Tree()
tree.insert(10)
tree.insert(7)
tree.insert(15)
tree.insert(20)
# print(tree.search(10))
# print(tree.search(20))
# print(tree.search(200))
# print(tree.breadth_first_search())
print(tree.depth_first_search_preOreder())
print(tree.depth_first_search_postOreder())
print(tree.depth_first_search_inOrder())

# ----------------------------------- BFS(Breadth First Search) -----------------------------------------
# visit all node at one level before moving to the next level
# It uses queue data structure


# ---------------------------------- DFS (Depth First Search) -------------------------------------------------
# Visit all node at current branch and then backtrack to other branch
# Three types of Dfs:
# 1) PreOrder: Follows VLR  (root is the first thing to be pushed)
# 2) Postorder: Folloes LRV  (root is the last thing to be pushed)
# 3) Inorder: Follows LVR (Gives sorted order)


# -------------------------------- BFS vs DFS ---------------------------------------------
# If tree contains all the left and right nod i.e it is a wide treee, here dfs shine out agianst bfs in space complexity
# In Special Case binary tree such as only left binary tree or right binary tree then BSF shiine out against dfs

# ---------------------------------------  Big O Notation ------------------------------------------------
# 1) Insertion: Best and average case O(logn) , worst case: O(n)
# 2) Searching: Best and average case O(logn), worst case: O(n)
# reason (for best and average case): When we double the number of nodes , you only increase the number of step to insert and find by 1
# reason (for worst case): Special Case binary tree such as only left binary tree or right binary tree , then to insert ans searching of node is directly propotional as tree grows
