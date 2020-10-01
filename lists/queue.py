from collections import deque


class Queue(object):
    """Wrapper around collections.deque to provide the api consistent with
    a Queue"""

    def __init__(self):
        self.items = deque()

    def __str__(self):
        return ("Queue of size: %d" % len(self.items))

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def printEle(self):
        return self.items


q = Queue()

while True:

    print("1. Enqueue \n 2. Dequeue \n 3. checkLength \n 4. Print \n 5.EXIT")

    num = int(input("Enter the operation on queue :"))

    if num == 1:

        data = int(input("Enter DATA :"))
        
        q.enqueue(data)

        print("ADDED SUCCESSFULLY")

    elif num == 2:

        print(q.dequeue())

    elif num == 3:

        print(q.__str__())

    elif num == 4:

        l = q.printEle()
        print(*l)

    elif num == 5:
        break

    else:
        print("Invalid Operation")
