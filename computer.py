from game_play import GamePlay
import random

gp = GamePlay()


class Machine:
    def __init__(self, player, sign):
        self.player = player
        self.sign = sign

    def first_level_game(self, board):
        for i in range(9):
            if i % 2 == 0:
                self.common_function_player(board)
            else:
                while True:
                    random_row, random_col = random.randint(1, 3), random.randint(1, 3)
                    if gp.insert_sign(board, random_row, random_col, 'O'):
                        print(f"\nKomputer wykonał ruch: wiersz {random_row}, kolumna {random_col}")
                        gp.print_board(board)
                        if gp.win_algorithm(board, 'O'):
                            print("\nKomputer wygrał!")
                            return
                        break

    def common_function_player(self, board):
        while True:
            try:
                row, col = map(int, input(
                    f"\n{self.player}, wprowadź współrzędne (wiersz i kolumna) oddzielone spacją: ").split())
                if gp.insert_sign(board, row-1, col-1, 'X'):
                    gp.print_board(board)
                    if gp.win_algorithm(board, 'X'):
                        print(f"\n{self.player} wygrał!")
                        return
                    break
                else:
                    print("Pole zajęte, spróbuj ponownie.")
            except ValueError:
                print("Nieprawidłowe współrzędne, wprowadź liczby.")

    # Упростити та зрозуміти алгоритм мінімакс
    def second_level_game(self, board):
        for i in range(9):
            if i % 2 == 0:
                self.common_function_player(board)
            else:
                while True:
                    best_move = gp.find_move(board)  # Виклик find_move
                    if best_move is None:  # Якщо find_move повернуло None
                        print("Gra zakończona, brak dostępnych ruchów.")
                        return
                    if gp.insert_sign(board, best_move[0], best_move[1], 'O'):
                        print(f"\nKomputer wykonał ruch: wiersz {best_move[0] + 1}, kolumna {best_move[1] + 1}")
                        gp.print_board(board)
                        if gp.win_algorithm(board, 'O'):
                            print("\nKomputer wygrał!")
                            return
                        break
