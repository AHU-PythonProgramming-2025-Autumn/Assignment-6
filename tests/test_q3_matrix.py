import math
from src.q3_matrix import Matrix2x2
from src.q2_vector2d import Vector2D


def test_multiply_vector_basic():
    m = Matrix2x2(1, 0, 0, 1)
    v = Vector2D(3, 4)
    result = m.multiply_vector(v)
    assert result.x == 3
    assert result.y == 4


def test_multiply_vector_general():
    m = Matrix2x2(2, 1, 1, 3)
    v = Vector2D(1, 2)
    result = m.multiply_vector(v)
    # x' = 2*1 + 1*2 = 4
    # y' = 1*1 + 3*2 = 7
    assert result.x == 4
    assert result.y == 7


def test_det():
    m = Matrix2x2(1, 2, 3, 4)
    assert m.det() == (1 * 4 - 2 * 3)   # -2


def test_is_invertible_true():
    m = Matrix2x2(1, 2, 3, 4)
    assert m.is_invertible() is True


def test_is_invertible_false():
    m = Matrix2x2(1, 2, 2, 4)  # 行列式 = 1*4 - 2*2 = 0
    assert m.is_invertible() is False


def test_float_type():
    m = Matrix2x2(1, 2, 3, 4)
    assert isinstance(m.a, float)
    assert isinstance(m.b, float)
    assert isinstance(m.c, float)
    assert isinstance(m.d, float)
