import pytest
from src.q1_bank import BankAccount


def test_deposit():
    acc = BankAccount("A01", 1000)
    acc.deposit(200)
    assert acc.balance == 1200


def test_withdraw():
    acc = BankAccount("A01", 1000)
    acc.withdraw(300)
    assert acc.balance == 700


def test_withdraw_insufficient():
    acc = BankAccount("A01", 100)
    with pytest.raises(ValueError):
        acc.withdraw(200)


def test_transfer():
    acc1 = BankAccount("A01", 1000)
    acc2 = BankAccount("A02", 500)
    acc1.transfer(acc2, 300)
    assert acc1.balance == 700
    assert acc2.balance == 800


def test_logs():
    acc = BankAccount("A01", 1000)
    acc.deposit(100)
    acc.withdraw(50)
    log_str = str(acc)
    assert "Deposit 100" in log_str
    assert "Withdraw 50" in log_str


def test_negative_deposit():
    acc = BankAccount("A01", 100)
    with pytest.raises(ValueError):
        acc.deposit(-1)


def test_negative_transfer():
    acc1 = BankAccount("A01", 1000)
    acc2 = BankAccount("A02", 1000)
    with pytest.raises(ValueError):
        acc1.transfer(acc2, -5)
