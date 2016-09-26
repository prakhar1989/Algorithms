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
