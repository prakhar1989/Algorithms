import pytest
from lists.singlylinkedlist import SinglyLinkedList

@pytest.fixture
def setup_list():
	tens = SinglyLinkedList(range(0, 100, 10))
	blankList = SinglyLinkedList()
	return (tens, blankList)

def test_length_method(setup_list):
	tens, blankList = setup_list
	assert len(tens) == 10
	assert len(blankList) == 0

def test_add_method(setup_list):
	tens, blankList = setup_list
	blankList.append(50)
	tens.append(110)
	assert len(blankList) == 1
	assert len(tens) == 11
