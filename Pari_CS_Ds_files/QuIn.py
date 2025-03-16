class Queue:
    def __init__(self):
        self.queue1 = [None] * 5  # Fixed-size array to hold queue elements
        self.rear = -1
        self.front = -1

    def insert(self, x):
        if self.rear >= 4:  # Prevent overflow
            print("Queue overflow")
            return
        self.rear += 1
        self.queue1[self.rear] = x
        print(f"Inserted: {x}")

    def delet(self):
        if self.front == self.rear:  # Check for underflow
            print("Queue underflow")
            return
        self.front += 1
        print(f"Deleted: {self.queue1[self.front]}")

    def display(self):
        if self.rear == self.front:  # Check if the queue is empty
            print("Queue is empty")
            return
        print("Queue elements:", end=" ")
        for i in range(self.front + 1, self.rear + 1):
            print(self.queue1[i], end=" ")
        print()


def main():
    qu = Queue()

    while True:
        print("\n1. Insert  2. Delete  3. Display  4. Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            value = int(input("Enter the element: "))
            qu.insert(value)
        elif ch == 2:
            qu.delet()
        elif ch == 3:
            qu.display()
        elif ch == 4:
            return  # Exit the program
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
