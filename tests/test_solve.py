import pytest

from core.math import solve


def test_solve():
    assert pytest.approx(10, 0.00001) == solve().tolist()[0]
    assert pytest.approx(15, 0.00001) == solve().tolist()[1]
