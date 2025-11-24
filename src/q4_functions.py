"""
出题者：柳文章，安徽大学人工智能学院
出题日期：2025.11.22

创建一个名为 ``Function`` 的父类，用来“描述所有函数应该有哪些行为”。

#### 父类内容：

- 方法：
  - value(x)
    - 在父类中不要写具体计算，只写一个提示或占位（如 pass 或返回 None）
    - 目的是让子类来重写这个方法
  - table(x_list)
    - 输入一个 x 的列表
    - 返回一个 f(x) 的列表
    - 必须使用子类重写后的 value(x) 来计算

#### 子类 1：LinearFunction

线性函数： $f(x)=ax+b$

属性：
- a
- b

#### 子类 2：QuadraticFunction

二次函数：$f(x)=ax^2+bx+c$

属性：
- a
- b
- c

#### 子类 3：ExponentialFunction

指数函数：$f(x) = ke^x$

属性：
- k

  提示：需要导入math模块来计算exp函数。
"""

import math


class Function:
    # 父类仅提供接口，不做实际计算
    # TODO: 按要求在下方完成程序


class LinearFunction(Function):
    # TODO: 按要求在下方完成程序


class QuadraticFunction(Function):
    # TODO: 按要求在下方完成程序


class ExponentialFunction(Function):
    # TODO: 按要求在下方完成程序
