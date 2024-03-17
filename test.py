#start

import pytest

def test_list_append():
    my_list = []
    my_list.append(1)
    assert my_list == [1]

@pytest.mark.parametrize("value", [1, 2, 3])
def test_list_contains(value):
    my_list = [1, 2, 3]
    assert value in my_list

def test_int_addition():
    result = 2 + 3
    assert result == 5

def test_int_negative():
    result = -5
    assert result < 0

def test_tuple_indexing():
    my_tuple = (1, 2, 3)
    assert my_tuple[0] == 1

def test_tuple_immutable():
    my_tuple = (1, 2, 3)
    with pytest.raises(TypeError):
        my_tuple[0] = 5
