import pytest
from heaps.minheap import minheap
from heaps.maxheap import maxheap
import random

@pytest.fixture
def setup_heap():
	h = minheap()
	m = maxheap()
	a = [random.choice(range(50)) for i in range(10)]
	h.build_heap(a)
	m.build_heap(a)
	return (h, m, a)

def test_heap_pop(setup_heap):
	h, m, a = setup_heap
	assert min(a) == h.heappop()
	assert max(a) == m.heappop()

def test_max_elements(setup_heap):
	h, m, a = setup_heap
	assert len(a) == h.max_elements()
	assert len(a) == m.max_elements()

def test_heap_sort(setup_heap):
	h, m, a = setup_heap
	sorted_h = [h.heappop() for i in range(h.max_elements())]
	sorted_m = [m.heappop() for i in range(m.max_elements())]
	assert sorted_h == sorted(a)
	assert sorted_m == sorted(a, reverse=True)

def test_heap_push_method(setup_heap):
	h, m, a = setup_heap
	h.heappush(-1)
	assert -1 == h.heappop()
	m.heappush(100)
	assert 100 == m.heappop()

