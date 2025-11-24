"""
出题者：柳文章，安徽大学人工智能学院
出题日期：2025.11.22

编写类 `BankAccount`，要求：

- 属性：账号（string）、余额（double）
- 方法：
  - deposit(amount)
  - withdraw(amount)（余额不足时抛异常）
  - transfer(target_account, amount)
- 所有操作都记录在日志列表中
- 打印时输出所有日志
"""


class BankAccount:
    # TODO: 按要求在下方完成程序


if __name__ == "__main__":
    acc = BankAccount("A01", 1000)  # 输入账户名称，余额，创建账户
    acc.deposit(200)  # 存储200块
    acc.withdraw(300)  # 取款300块
    acc.withdraw(2000)  # 取款额度超出余额，会报错

    acc2 = BankAccount("A02", 500)  # 创建另外一个账户
    acc.transfer(acc2, 300)  # 向另外一个账户转账

    log_str = str(acc)  # 查看存取日志。提示：可使用__str__方法实现日志打印
