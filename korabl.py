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


class Menu:
    """Класс для работы пользовательского меню."""

    def print_main_menu(self) -> None:
        print(
            '\n1: Вывод информации о корабле.\n'
            '2: Изменить наименование корабля.\n'
            '3: Изменить водоизмещение корабля.\n'
            '4: Изменить тип корабля.\n'
            '5: Получить информацию о наименовании корабля.\n'
            '6: Получить информацию о водоизмещении корабля.\n'
            '7: Получить информацию о типе корабля.\n'
            '8: Корабль является военным?.\n'
            '9: Получить информацию о классе корабля\n'
            '0: ВЫХОД\n'
        )

    def main_menu(self, choice: int, ship: Ship) -> bool:

        is_running = True

        match choice:
            case 0:
                is_running = False

            case 1:
                ship.print_info()

            case 2:
                name = input('Введите наименование корабля: ')
                ship.set_name(name)

            case 3:
                displacement = int(
                    input('Введите водоизмещение корабля(учтите, что водоизмещение > 0): ')
                )
                ship.set_displacement(displacement)

            case 4:
                type_val = input('Введите тип корабля: ')
                ship.set_type(type_val)

            case 5:
                print(ship.get_name())

            case 6:
                print(ship.get_displacement())

            case 7:
                print(ship.get_type())

            case 8:
                if ship.is_military():
                    print('Да')
                else:
                    print('Нет')

            case 9:
                print(ship.get_ship_class())

        return is_running

ship_1 = Ship("Титаник", 55310, "Пассажирский пароход")
ship_2 = Ship()
menu = Menu()


def run() -> None:
    is_running = True

    while is_running:
        menu.print_main_menu()

        choice = int(input('Введите выбор: '))
        choice_ship = int(input('Введите порядковый номер корабля: '))

        ship = ship_1 if choice_ship == 1 else ship_2

        is_running = menu.main_menu(choice, ship)


run()
