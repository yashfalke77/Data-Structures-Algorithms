class Queue():
    def __init__(self, limit) -> None:
        self.queue = []
        self.limit = limit

    def empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def full(self):
        if len(self.queue) == self.limit:
            return True
        else:
            return False

    def push(self, x):
        if self.full():
            print("Queue is full")
        else:
            self.queue.append(x)

    def pop(self):
        if self.empty():
            print("Queue is empty")
        else:
            self.queue.pop(0)

    def show(self):
        if self.empty():
            print("queue is empty")
        else:
            print(f"Queue contains: {self.queue}")


def test_queue():
    limit = int(input("Enter the limit of your Queue: "))
    queue = Queue(limit)
    while True:
        print("1. push  2.pop  3.show  4.exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            x = int(input("Enter the number to be pushed: "))
            queue.push(x)
        elif choice == 2:
            queue.pop()
        elif choice == 3:
            queue.show()
        elif choice == 4:
            break


test_queue()


# ---------------------- Big O of Queue
# Insertion: O(1)
# Removal: O(1)
# Searching: O(N)
# Access: O(N)
