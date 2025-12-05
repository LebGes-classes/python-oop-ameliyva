from Ship import (
    Ship,
)


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