from src.q4_functions import Function, LinearFunction, QuadraticFunction, ExponentialFunction


def test_linear_value():
    f = LinearFunction(2, 1)  # f(x) = 2x + 1
    assert f.value(3) == 7


def test_quadratic_value():
    f = QuadraticFunction(1, 0, -1)  # f(x) = x^2 - 1
    assert f.value(2) == 3


def test_exponential_value():
    f = ExponentialFunction(3)  # f(x) = 3e^x
    assert round(f.value(0), 3) == 3.000


def test_table_polymorphism():
    funcs = [
        LinearFunction(1, 0),
        QuadraticFunction(1, 0, 0)
    ]
    results = [f.table([1, 2]) for f in funcs]

    # 线性函数 f(x)=x → [1,2]
    assert results[0] == [1, 2]

    # 二次函数 f(x)=x^2 → [1,4]
    assert results[1] == [1, 4]


def test_parent_value_none():
    # 父类应当返回 None
    f = Function()
    assert f.value(10) is None
