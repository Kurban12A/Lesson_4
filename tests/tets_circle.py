import pytest

from functions_my.func_circles import my_circle_square, my_circle_perimetr

def test_circle_sqaure():
    assert my_circle_square(5) == 78.53981633974483

def test_circle_sqaure_1():
    with pytest.raises(Exception):
        assert my_circle_square(5) == -1

def test_circle_perimetr():
    assert my_circle_perimetr(5) == 31.41592653589793

def test_circle_perimetr_1():
    with pytest.raises(Exception):
        assert my_circle_perimetr(5) == -1

