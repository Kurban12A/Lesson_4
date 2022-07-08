import pytest

from functions_my.funck_rectangle import my_reactangle_square, my_reactangle_perimetr

def test_my_reactangle_square():
    assert my_reactangle_square(10, 5) == 50

def test_my_reactangle_square_1():
    with pytest.raises(Exception):
        assert my_reactangle_square(0, -1) == -1

def test_my_reactangle_perimetr():
    assert my_reactangle_perimetr(10, 5) == 30

def test_my_reactangle_perimetr_1():
    with pytest.raises(Exception):
        assert my_reactangle_perimetr(-1, -1) == -1