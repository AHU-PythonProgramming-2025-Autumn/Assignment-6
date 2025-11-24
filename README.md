# Python Programming Assignment 6

## 🎯 作业目标
通过 5 道编程题目，巩固 Python 中的``面向对象程序设计``及``文件操作``。

## 任务 1：银行账户管理

编写类 `BankAccount`，要求：

- 属性：账号（string）、余额（double）
- 方法： 
  - deposit(amount)
  - withdraw(amount)（余额不足时抛异常） 
  - transfer(target_account, amount)
- 所有操作都记录在日志列表中 
- 打印时输出所有日志

### 任务 2：向量基础运算类

实现一个 二维向量类 ``Vector2D`` 并完成数学运算。

包含内容：
- 属性：
  - x (float)
  - y (float)
- 方法：
  - norm()：返回向量的欧氏长度 
  - add(other)：向量加法 
  - dot(other)：点积 
  - transform(matrix)：使用 2×2 矩阵变换向量


### 任务 3：矩阵运算类

实现一个 2×2 矩阵类 ``Matrix2x2``，并完成数学运算。

包含内容：
- 属性：
  - a, b, c, d (float)
- 方法：
  - multiply_vector(v)：返回该矩阵和向量 v 相乘后的结果
  - det()：返回该矩阵的行列式 
  - is_invertible()：判断该矩阵行列式是否为0

### 任务 4：函数类体系

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

### 任务5：文件操作

请设计一个类 ``TextFileAnalyzer``，用于分析纯文本文件（例如 .txt）。

类应包含以下功能：
- 构造方法
- 方法 1：读取整个文件内容
- 方法 2：统计行数
- 方法 3：统计单词数量
- 方法 4：统计某个单词出现次数（不区分大小写）

## 本地运行与测试

### 运行单题

```bash
python src/q1_bank.py
```

### 运行全部测试

```bash
pip install -r requirements.txt
pytest -q
```

    GitHub Classroom 会自动运行这些测试，检测程序输出是否正确。

## 注意事项

- 请勿修改 `tests/` 文件夹里的内容。
- 代码要加注释，变量命名清晰。
- 所有题目必须使用函数封装； 
- 每位同学的作业均独立完成，禁止抄袭； 
- 提交前确认测试全部通过。


```bash
出题人：柳文章 安徽大学人工智能学院
出题时间：2025.11.22
```
