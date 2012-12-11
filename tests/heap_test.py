import os, sys
sys.path.append(os.path.join(os.getcwd(), os.path.pardir))
import unittest
from heaps.minheap import minheap
from heaps.maxheap import maxheap
import random

class test_heap(unittest.TestCase):

    def setUp(self):
        self.h = minheap()
        self.m = maxheap()
        self.a = [random.choice(range(50)) for i in range(10)]
        self.h.build_heap(self.a)
        self.m.build_heap(self.a)

    def test_heap_pop(self):
        self.assertEqual(min(self.a), self.h.heappop())
        self.assertEqual(max(self.a), self.m.heappop())
    
    def test_max_elements(self):
        self.assertEqual(len(self.a), self.h.max_elements())
        self.assertEqual(len(self.a), self.m.max_elements())

    def test_heap_sort(self):
        sorted_h = [self.h.heappop() for i in range(self.h.max_elements())]
        sorted_m = [self.m.heappop() for i in range(self.m.max_elements())]
        self.assertEqual(sorted_h, sorted(self.a))
        self.assertEqual(sorted_m, sorted(self.a, reverse=True))

    def test_heap_push_method(self):
        self.h.heappush(-1)
        self.assertEqual(-1, self.h.heappop())
        self.m.heappush(100)
        self.assertEqual(100, self.m.heappop())

if __name__ == "__main__":
    unittest.main()
