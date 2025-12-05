from Ship import (
    Ship,
)
from Menu import (
    Menu,
)


ship_1 = Ship1("Титаник", 55310, "Пассажирский пароход")
ship_2 = Ship1()
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
