class doublylinkedlist:
    class _Node:
        __slots__ = '_data', '_prev', '_next'


        def __init__(self, data, prev, next):
            self._data = data
            self._prev = prev
            self._next = next


    def __init__(self):
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._tail._prev = self._head
        self._head._next = self._tail
        self._size = 0


    def is_empty(self):
        return self._size == 0


    def add_first(self, value):
        new_node = self._Node(value, None, None)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next = self._head
            self._head._prev = new_node
        self._head = new_node
        self._size += 1


    def add_last(self, value):
        new_node = self._Node(value, None, None)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail._next = new_node
            new_node._prev = self._tail
        self._tail = new_node
        self._size += 1


    def add_particular_position(self, value, position):
        new_node = self._Node(value, None, None)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            temp = self._head
            i = 1
            while i < position-1:
                temp = temp._next
                i += 1
            new_node._next = temp._next
            new_node._prev = temp
            temp._next._prev = new_node
            temp._next = new_node
        self._size += 1


    def remove_first(self):
        if self.is_empty():
            print("The list is empty")
        value = self._head._data
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return value


    def remove_last(self):
        if self.is_empty():
            print("The list is empty")
        value = self._tail._data
        self._tail = self._tail._prev
        self._tail._next = None
        self._size -= 1
        if self.is_empty():
            self._head = None
        return value


    def remove_particular(self, position):
        if self.is_empty():
            print("The list is empty")
        i = 1
        temp = self._head
        while i < position-1:
            temp = temp._next
            i += 1
        value = temp._next._data
        temp._next._next._prev = temp
        temp._next = temp._next._next
        self._size -= 1
        return value


    def print_forward(self):
        temp = self._head
        while temp:
            print(temp._data, end='-->')
            temp = temp._next
        print()


    def print_backward(self):
        temp = self._tail
        while temp:
            print(temp._data, end='<--')
            temp = temp._prev
        print()


dll = doublylinkedlist()
dll.add_last(8)
dll.add_first(2)
dll.add_particular_position(3, 2)
dll.add_first(1)
dll.add_particular_position(5, 4)
dll.add_particular_position(4, 4)
dll.add_particular_position(6, 6)
dll.add_particular_position(7, 7)
dll.print_forward()
dll.print_backward()
print(dll.remove_last())
print(dll.remove_first())
dll.print_forward()
dll.print_backward()
print(dll.remove_particular(3))
dll.print_forward()
dll.print_backward()