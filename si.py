import structure
from structure import GamePlay
import random

gp = GamePlay()


class Machine:
    def __init__(self, player, sign):
        self.player = player
        self.sign = sign

    def first_level_game(self, board):
        for i in range(9):
            if i % 2 == 0:
                while True:
                    try:
                        row, col = map(int, input(
                            f"\n{self.player}, введіть координати (рядок і стовпець) через пробіл: ").split())
                        if gp.insert_sign(board, row, col, 'X'):
                            gp.print_board(board)
                            if gp.win_algorithm(board, 'X'):
                                print(f"\n{self.player} переміг!")
                                return
                            break
                        else:
                            print("Поле зайняте, спробуйте ще раз.")
                    except ValueError:
                        print("Неправильна координата, введіть числа.")
            else:
                while True:
                    random_row, random_col = random.randint(1, 3), random.randint(1, 3)
                    if gp.insert_sign(board, random_row, random_col, 'O'):
                        print(f"\nКомп'ютер зробив хід: рядок {random_row}, стовпець {random_col}")
                        gp.print_board(board)
                        if gp.win_algorithm(board, 'O'):
                            print("\nКомп'ютер переміг!")
                            return
                        break
# Упростити та зрозуміти алгоритм мінімакс
    def second_level_game(self, board):
        for i in range(9):
            if i % 2 == 0:
                while True:
                    try:
                        row, col = map(int, input(
                            f"\n{self.player}, введіть координати (рядок і стовпець) через пробіл: ").split())
                        if gp.insert_sign(board, row, col, 'X'):
                            gp.print_board(board)
                            if gp.win_algorithm(board, 'X'):
                                print(f"\n{self.player} переміг!")
                                return
                            break
                        else:
                            print("Поле зайняте, спробуйте ще раз.")
                    except ValueError:
                        print("Неправильна координата, введіть числа.")
            else:
                while True:
                    best_move = gp.find_move(board)  # Виклик find_move
                    if best_move is None:  # Якщо find_move повернуло None
                        print("Гра завершена, немає доступних ходів.")
                        return
                    if gp.insert_sign(board, best_move[0] + 1, best_move[1] + 1, 'O'):
                        print(f"\nКомп'ютер зробив хід: рядок {best_move[0] + 1}, стовпець {best_move[1] + 1}")
                        gp.print_board(board)
                        if gp.win_algorithm(board, 'O'):
                            print("\nКомп'ютер переміг!")
                            return
                        break

