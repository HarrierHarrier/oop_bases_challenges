"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float):
        self.balance += amount

    def decrease_balance(self, amount: float):
        self.balance -= amount


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == '__main__':
    bank_account = BankAccount(
        owner_full_name='Daniel A. Enaorch',
        balance=2500
    )
    print(bank_account.balance)
    bank_account.increase_balance(100)
    print(bank_account.balance)
    bank_account.decrease_balance(250)
    print(bank_account.balance)

    credit_account = CreditAccount(
        owner_full_name='Daniel A. Enaorch',
        balance=2500
    )
    print(credit_account.balance)
    bank_account.increase_balance(100)
    print(credit_account.balance)
    bank_account.decrease_balance(250)
    print(credit_account.balance)
    print(credit_account.is_eligible_for_credit())
