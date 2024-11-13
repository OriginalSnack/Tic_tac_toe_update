from structure import GamePlay
from si import Machine

# інструкція
instructions = """To będzie nasza plansza do gry w kółko i krzyżyk (tic tac toe)

 (1 1) | (1 2) | (1 3) 
-------|-------|------
 (2 1) | (2 2) | (2 3) 
-------|-------|------
 (3 1) | (3 2) | (3 3) 

*instrukcje:

0. Masz wybór: grać ze sztuczną inteligencją albo z kolegą.
1. Masz wybór: rozpocznij nową grę lub kontynuuj od ostatniego punktu zapisu.
2. Wprowadź parę liczb (1 3), aby umieścić swój znak.
3. Musisz wypełnić wszystkie pola, aby uzyskać wynik.
4. Gracz 1 zaczyna pierwszy.
"""

# обєкт класу Gameplay()
gp = GamePlay()


def game(board):
    # дошкa
    player1 = input(f"\nВведіть назву першого користувача: ")
    player2 = input("Введіть назву другого користувача: ")
    players = [player1, player2]
    signs = ['X', 'O']

    for i in range(9):
        current_player = players[i % 2]
        current_sign = signs[i % 2]
        while True:
            try:
                row, col = map(int, input(
                    f"\n{current_player}, введіть координати (рядок і стовпець) через пробіл: ").split())
                if gp.insert_sign(board, row, col, current_sign):
                    gp.print_board(board)
                    if gp.win_algorithm(board, current_sign):
                        print(f"\n{current_player} переміг!")
                        return
                    break
                else:
                    print("Поле зайняте, спробуйте ще раз.")
            except ValueError:
                print("Неправильна координата, введіть числа.")

    print("\nНічия")


# Основна функція запуску
def main():
    sign_dict = [[' ' for _ in range(3)] for _ in range(3)]
    print(instructions)
    while (True):
        try:
            choise = int(input(f"\nРежим гри 1 (з людиною) або 2 (з комп'ютером): "))
            if choise == 1:
                game(sign_dict)
                break
            elif choise == 2:
                print("Режим гри з комп'ютером у розробці...")
                player12 = input("Введи своє ім`я: ")
                level_game = input("Введіть рівень складності: 1(слабо) та 2(складно): ")
                si = Machine(player12, 'O')
                if level_game == 1:
                    si.first_level_game(sign_dict)
                else:
                    si.second_level_game(sign_dict)
                break
            else:
                print("Невірне введення, спробуйте ще раз")
        except ValueError:
            print("Невірне введення, спробуйте ще раз")


if __name__ == "__main__":
    main()
