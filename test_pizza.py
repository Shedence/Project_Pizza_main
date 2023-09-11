import pytest
from pizza import Margherita, Hawaiian, Pepperoni


def test_pizza_equality():
    pizza1 = Pepperoni("L")
    pizza2 = Pepperoni("L")
    pizza3 = Margherita("L")
    assert pizza1 == pizza2
    assert pizza1 != pizza3


@pytest.mark.parametrize(
    "pizza_class, name, size",
    [(Margherita, "Margherita", "L"), (Pepperoni, "Pepperoni", "L"), (Hawaiian, "Hawaiian", "L"),],
    )
def test_pizza_default(pizza_class, name: str, size: str):
    pizza = pizza_class(size)
    assert pizza_class.__name__ == name
    assert pizza.size == size

def test_pizza_ingredients():
    ingredients={}
    ingredients["tomato sauce"] = 200
    ingredients["mozzarella"] = 250
    ingredients["pepperoni"] = 140
    assert Pepperoni("XL")._ingredients == ingredients


def test_wrong_size():
    with pytest.raises(ValueError):
        Pepperoni("S")


def test_change_size():
    pizza_test = Pepperoni("XL")
    with pytest.raises(ValueError):
        pizza_test.size="M"
