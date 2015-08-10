class Queue(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        return ("Queue of size: %d" % len(self.items))

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

