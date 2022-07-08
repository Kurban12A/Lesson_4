import pytest

from functions_my.funk_triangle import my_triange_square, my_triange_perimetr

def test_my_triange_square():
    assert my_triange_square(10, 5) == 25.0

def test_my_triange_square_1():
    with pytest.raises(Exception):
        assert my_triange_square(0, -1) == -1

def test_my_triange_perimetr():
    assert my_triange_perimetr(10, 5, 5) == 20

def test_my_triange_perimetr_1():
    with pytest.raises(Exception):
        assert my_triange_perimetr(-1, -1, -1) == -1