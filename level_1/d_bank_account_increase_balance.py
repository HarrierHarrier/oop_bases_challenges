"""
У нас есть класс банковского аккаунта со свойсвами: полное имя владельца и баланс, но не релизован
метод, который увеливает баланс.

Задания:
    1. Допишите логику в метод increase_balance, который должен увеличивать баланс банковского счета на значение income.
    2. Создайте экземпляр класса банковского счета и распечатайте баланс.
    3. Увеличьте баланс счета у экземпляра класса с помощью метода increase_balance и снова распечтайте текущий баланс.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income


if __name__ == '__main__':
    account = BankAccount(
        owner_full_name='Daniel A. Enaorch',
        balance=10500000.0
    )
    print(f"Balance: {account.balance}")

    account.increase_balance(300.0)
    print(f"Increased balance: {account.balance}")
