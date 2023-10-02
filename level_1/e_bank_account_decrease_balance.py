"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income

    def decrease_balance(self, spending: float):
        result = self.balance - spending
        if result < 0:
            raise ValueError("Spending cannot exceed current balance.")
        self.balance = result


if __name__ == '__main__':
    account = BankAccount(
        owner_full_name='Daniel A. Enaorch',
        balance=10500000.0
    )
    account.decrease_balance(1e7)
    print(f"Balance: {account.balance}")

    account.decrease_balance(7e5)
    print(f"Balance: {account.balance}")
