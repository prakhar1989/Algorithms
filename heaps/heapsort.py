from minheap import minheap
import random

def heapsort(nums):
    h = minheap(nums)
    return [h.heappop() for i in range(h.max_elements())]

if __name__ == "__main__":
    a = [random.choice(range(100)) for i in range(40)]
    print heapsort(a) == sorted(a)
