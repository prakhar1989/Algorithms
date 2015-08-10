class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class SinglyLinkedList(object):
    def __init__(self, iterable=[]):
        self.head = None
        self.size = 0
        for item in iterable: self.append(item)

    def __repr__(self):
        (current, nodes) = self.head, []
        while current:
            nodes.append(str(current))
            current = current.next
        return "->".join(nodes)

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
        raise StopIteration

    def __contains__(self, data):
        tmp = self.head
        found = False
        while tmp and not found:
            if data == tmp.data:
                found = True
            else:
                tmp = tmp.next
        return found

    def append(self, data):
        tmp = Node(data)
        tmp.next = self.head
        self.head = tmp
        self.size += 1

    def getHead(self):
        return self.head

    def getTail(self):
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        return tmp

    def delete(self, data):
        tmp = self.head
        prev = None
        found = False
        while tmp and not found:
            if data == tmp.data:
                found = True
            else:
                prev = tmp
                tmp = tmp.next
        if found:
            self.size -= 1
            if prev == None:
                self.head = self.head.next
            else:
                prev.next = tmp.next

if __name__ == "__main__":
    list1 = SinglyLinkedList(range(0, 100, 10))
    print list1 # testing repr
    print 50 in list1, 110 not in list1 # testing contains
    list1.delete(50) # testing delete
    print len(list1) == 9, 50 not in list1 # testing size
