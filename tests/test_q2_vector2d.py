from src.q2_vector2d import Vector2D


def test_norm():
    v = Vector2D(3, 4)
    assert v.norm() == 5.0


def test_add():
    v1 = Vector2D(1, 2)
    v2 = Vector2D(3, 4)
    v3 = v1.add(v2)
    assert v3.x == 4
    assert v3.y == 6


def test_dot():
    v1 = Vector2D(1, 2)
    v2 = Vector2D(3, 4)
    assert v1.dot(v2) == 11


def test_transform_identity():
    v = Vector2D(5, 7)
    m = [[1, 0], [0, 1]]
    v2 = v.transform(m)
    assert v2.x == 5
    assert v2.y == 7


def test_transform_general():
    v = Vector2D(2, 3)
    m = [[2, 1], [1, 2]]  # 常见线性变换
    v2 = v.transform(m)
    assert v2.x == 2*2 + 1*3   # 7
    assert v2.y == 1*2 + 2*3   # 8


def test_float_type():
    v = Vector2D(1, 2)
    assert isinstance(v.x, float)
    assert isinstance(v.y, float)
