"""
出题者：柳文章，安徽大学人工智能学院
出题日期：2025.11.22

实现一个 2×2 矩阵类 ``Matrix2x2``，并完成数学运算。

包含内容：
- 属性：
  - a, b, c, d (float)
- 方法：
  - multiply_vector(v)：返回该矩阵和向量 v 相乘后的结果
  - det()：返回该矩阵的行列式
  - is_invertible()：判断该矩阵行列式是否为0
"""

from src.q2_vector2d import Vector2D


class Matrix2x2:
    # TODO: 按要求在下方完成程序


if __name__ == "__main__":
    # 运行示例：
    m = Matrix2x2(1, 0, 0, 1)
    v = Vector2D(3, 4)
    result = m.multiply_vector(v)
