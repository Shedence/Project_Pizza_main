from enum import Enum


class PizzaSize(Enum):
    L = 0
    XL = 1


class Pizza:
    def __init__(self, size: str) -> None:
        self._size = size
        ingredients = {}
        if self._size == "L":
            ingredients["tomato sauce"] = 100
            ingredients["mozzarella"] = 150
        elif self._size == "XL":
            ingredients["tomato sauce"] = 200
            ingredients["mozzarella"] = 250
        else:
            raise ValueError("There is no such size in menu")
        self._ingredients = ingredients

    @property
    def size(self) -> str:
        return self._size

    def dict(self) -> dict:
        return self._ingredients

    @size.setter
    def size(self, new_size: str):
        """Проверка на присвоение"""
        if isinstance(new_size, PizzaSize) is True:
            return
        else:
            self._size = new_size
            raise ValueError("There is no such size in menu")

    def __eq__(self, other) -> bool:
        return self._size == other._size and self._ingredients == other._ingredients

    """Для чего это понадобилось? Дело в том, что первоначально нужная запись в словаре ищется по хэшу, " \
    "так как существует быстрый алгоритм поиска нужного значения хэша. А, затем, для равных хешей (если такие были " \
    "обнаружены), отбирается запись с указанным в ключе объекте. Такой подход значительно ускоряет поиск значения в " \
    "словаре."""

    def __hash__(self) -> int:
        return hash((self._size, str(self._ingredients)))


class Margherita(Pizza):

    def __init__(self, size: str) -> None:
        super().__init__(size)
        if self._size == "L":
            self._ingredients["tomatoes"] = 50
        elif self.size == "XL":
            self._ingredients["toma toes"] = 100


class Pepperoni(Pizza):

    def __init__(self, size: str) -> None:
        super().__init__(size)
        if self._size == "L":
            self._ingredients["pepperoni"] = 70
        elif self.size == "XL":
            self._ingredients["pepperoni"] = 140


class Hawaiian(Pizza):

    def __init__(self, size: str) -> None:
        super().__init__(size)
        if self._size == "L":
            self._ingredients["chicken"] = 110
            self._ingredients["pineapple"] = 30

        elif self.size == "XL":
            self._ingredients["chicken"] = 220
            self._ingredients["pineapple"] = 60
