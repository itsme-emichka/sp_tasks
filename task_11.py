class Dessert:
    def __init__(
            self,
            name: str | None = None,
            calories: int | None = None
    ) -> None:
        self._name = name
        self._calories = calories

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise Exception
        self._name = value

    @property
    def calories(self) -> int:
        return self._calories

    @calories.setter
    def calories(self, value: int) -> None:
        self._calories = value

    def is_healthy(self) -> bool:
        return isinstance(self._calories, int) and self._calories < 200

    def is_delicious(self) -> bool:
        return True


if __name__ == '__main__':
    dessert = Dessert('cake', 100)

    print(dessert.name)
    dessert.name = 'potato'
    print(dessert.name)

    print(dessert.calories)
    print(dessert.is_healthy())
    dessert.calories = 300
    print(dessert.calories)
    print(dessert.is_healthy())

    print(dessert.is_delicious())
