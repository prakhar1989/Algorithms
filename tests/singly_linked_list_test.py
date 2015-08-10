import os, sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
import unittest
from lists.singlylinkedlist import SinglyLinkedList

class test_graph(unittest.TestCase):
    def setUp(self):
        self.tens = SinglyLinkedList(range(0, 100, 10))
        self.blankList = SinglyLinkedList()

    def test_length_method(self):
        self.assertEqual(len(self.tens), 10)
        self.assertEqual(len(self.blankList), 0)

    def test_add_method(self):
        self.blankList.append(50)
        self.tens.append(110)
        self.assertEqual(len(self.blankList), 1)
        self.assertEqual(len(self.tens), 11)

if __name__ == "__main__":
    unittest.main()
