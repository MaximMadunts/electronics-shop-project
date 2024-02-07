from src.phone import Phone


def test_phone_creation():
    phone = Phone("Samsung Galaxy", 80000, 3, 1)
    assert phone.name == "Samsung Galaxy"
    assert phone.price == 80000
    assert phone.quantity == 3
    assert phone.number_of_sim == 1


def test_phone_representation():
    phone = Phone("Samsung Galaxy", 80000, 3, 1)
    assert repr(phone) == "Phone('Samsung Galaxy', 80000, 3, 1)"
    assert str(phone) == "Samsung Galaxy"


def test_phone_addition():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("Samsung Galaxy", 80_000, 3, 1)
    result = phone1 + phone2
    assert result == 8

