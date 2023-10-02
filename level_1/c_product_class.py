"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""
from decimal import Decimal


class Product:
    def __init__(
        self, name: str, description: str, price: Decimal, weight: Decimal
    ) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight


if __name__ == '__main__':
    product = Product(
        name='Пончик с повидлом',
        description='Пончик с начинкой из фруктового повидла.',
        price=Decimal('120.00'),
        weight=Decimal('75.00')
    )
    print(
        f"Информация о продукте: {product.name}, {product.description},"
        f" {product.price}, {product.weight}"
    )
