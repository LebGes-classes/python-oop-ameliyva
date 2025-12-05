class Ship:
    """Класс для описания корабля."""

    def __init__(self, name: str = "NA", displacement=1, type: str = "NA") -> None:
        """Инициализация класса.

        Args:
            name: Наименование корабля.
            displacement: Водоизмещение корабля.
            type: Тип корабля.
        """

        self.__name = name
        self.__displacement = displacement
        self.__type = type

    def set_name(self, name: str) -> None:
        """Сеттер для наименования корабля.

        Args:
            name: Наименование корабля.
        """

        self.__name = name

    def get_name(self) -> str:
        """Геттер для наименования корабля.

        Returns:
            name: Наименование корабля
        """

        return self.__name

    def set_displacement(self, displacement) -> None:
        """Сеттер для водоизмещения корабля.

        Args:
            displacement: Водоизмещение корабля.
        """

        self.__displacement = displacement

        if displacement <= 0:
            print('Введите корректное значение. Учтите, водоизмещение => 0: ')
            self.__displacement = 1

    def get_displacement(self):
        """Геттер для водоизмещения корабля.

        Returns:
            displacement: Водоизмещение корабля.
        """

        return self.__displacement

    def set_type(self, type: str) -> None:
        """Сеттер для типа корабля.

        Args:
            type: Тип корабля.
        """

        self.__type = type

    def get_type(self) -> str:
        """Геттер для типа корабля.

        Returns:
            type: Тип корабля.
        """

        return self.__type

    def print_info(self) -> None:
        """Вывод информации о корабле."""

        print(
            f'\nНаименование корабля: {self.get_name()}\n'
            f'Водоизмещение корабля: {self.get_displacement()}\n'
            f'Тип корабля: {self.get_type()}\n'
        )

    def get_ship_class(self):
        """Определяет класс корабля по его водоизмещению."""

        if self.__displacement < 1000:

            return "Малый корабль"

        elif self.__displacement < 5000:

            return "Средний корабль"

        elif self.__displacement < 20000:

            return "Большой корабль"

        else:

            return "Очень большой корабль"

    def is_military(self) -> bool:
        """Проверяет, военный корабль или нет.

        Returns:
            bool: True - военный, False - нет.
        """
        if self.__type.lower() in ["эсминец", "крейсер", "авианосец",
                                   "фрегат", "корвет", "подлодка"]:

            return True
        else:

            return False
