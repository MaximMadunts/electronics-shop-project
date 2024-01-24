from src.item import Item


"""Здесь надо написать тесты с использованием pytest для модуля item."""

def test_calculate_total_price():
    item = Item(name="Test Item", price=10.0, quantity=5)
    total_price = item.calculate_total_price()
    expected_price = 10.0 * 5
    assert total_price == expected_price
    assert item in Item.all

def test_apply_discount():
    item = Item(name="Test Item", price=10.0, quantity=5)
    item.apply_discount()
    discounted_price = 10.0 * item.pay_rate
    assert item.price == discounted_price

def test_apply_discount_multiple_items():
    item1 = Item(name="Item 1", price=10.0, quantity=3)
    item2 = Item(name="Item 2", price=15.0, quantity=2)

    item1.apply_discount()
    discounted_price_item1 = 10.0 * item1.pay_rate
    assert item1.price == discounted_price_item1

    assert item2.price == 15.0  # apply_discount не должен влиять на другие товары


