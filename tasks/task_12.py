from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(
            self,
            name: str | None = None,
            calories: int | None = None,
            flavor: str | None = None
    ) -> None:
        super().__init__(name, calories)
        self._flavor = flavor
        self.not_delicious_flavor = 'black licorice'

    @property
    def flavor(self) -> str:
        return self._flavor

    @flavor.setter
    def flavor(self, value: str) -> None:
        if not isinstance(value, str):
            raise Exception
        self._flavor = value

    def is_delicious(self) -> bool:
        return not self._flavor == self.not_delicious_flavor


if __name__ == '__main__':
    dessert = JellyBean(
        'name',
        300,
        'flavor'
    )

    print(dessert.flavor)
    print(dessert.is_delicious())
    dessert.flavor = 'black licorice'
    print(dessert.flavor)
    print(dessert.is_delicious())
