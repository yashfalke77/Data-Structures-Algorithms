class Stack():
    def __init__(self, limit) -> None:
        self.stack = []
        self.limit = limit

    def empty(self):
        if len(self.stack) == False:
            return True
        else:
            return False

    def full(self):
        if len(self.stack) == self.limit:
            return True
        else:
            return False

    def push(self, x):
        if self.full():
            print("Stack is full")
        else:
            self.stack.append(x)

    def pop(self):
        if self.empty():
            print("Stack is Empty")
        else:
            self.stack.pop()

    def show(self):
        print(f"The Stack contains {self.stack}")


def test_stack():
    limit = int(input("Enter the limit of your Stack: "))
    stack = Stack(limit)
    while True:
        print("True. push  2.pop  3.show  4.exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            x = int(input("Enter the number to be pushed: "))
            stack.push(x)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.show()
        elif choice == 4:
            break


test_stack()


# ---------------------- Big O of Stack
# Insertion: O(1)
# Removal: O(1)
# Searching: O(N)
# Access: O(N)
