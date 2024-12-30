import random
from game_play import GamePlay

'''
    Klas Machine zawiera funkcji dla możliwości grać z komputerom
    Są dwa poziomy trudności
    1 - łatwy 
    2 - trudny
'''


class Machine:
    '''
        Konstruktor ma dwa parametry - player(gracz),sign(znak)
    '''

    def __init__(self, player, sign, gameplay):
        self.player = player
        self.sign = sign
        self.gp = gameplay

    '''
        Pierwszy poziom trudności działa za pomocą biblioteky random
        komputer wstawia znak losowo
    '''

    def first_level_game(self, board):
        for i in range(9):
            if self.gp.win_algorithm(board, 'X') or self.gp.win_algorithm(board, 'O'):
                return
            if i % 2 == 0:
                self.common_function_player(board)
            else:
                while True:
                    random_row, random_col = random.randint(0, 2), random.randint(0, 2)
                    if self.gp.insert_sign(board, random_row, random_col, 'O'):
                        print(f"\nKomputer wykonał ruch: wiersz {random_row + 1}, kolumna {random_col + 1}")
                        self.gp.print_board(board)
                        if self.gp.win_algorithm(board, 'O'):
                            print("\nKomputer wygrał!")
                            return
                        break

    '''
         Common_function_player jest funkcją wspólną dla pierwszego i drugiego poziomu trudności
         Dlatego umieściłem ruch gracza do innej funkcji aby uprościć kod
    '''

    def common_function_player(self, board):
        while True:
            try:
                row, col = map(int, input(
                    f"\n{self.player}, wprowadź współrzędne (wiersz i kolumna) oddzielone spacją: ").split())
                if 1 <= row <= 3 and 1 <= col <= 3:
                    if self.gp.insert_sign(board, row - 1, col - 1, 'X'):
                        self.gp.print_board(board)
                        if self.gp.win_algorithm(board, 'X'):
                            print(f"\n{self.player} wygrał!")
                            return
                        break
                    else:
                        print("Pole zajęte, spróbuj ponownie.")
                else:
                    print("Wprowadź liczby od 1 do 3.")
            except ValueError:
                print("Nieprawidłowe współrzędne, wprowadź liczby.")

    '''
        Drugi poziom trudności działa za pomocą funkcji minimaks w klasie GamePlay
        komputer rekurencyjnie oblicza wszystkie pozycje i wstawia znak
    '''

    def second_level_game(self, board):
        for i in range(9):
            if self.gp.win_algorithm(board, 'X') or self.gp.win_algorithm(board, 'O'):
                return
            if i % 2 == 0:
                self.common_function_player(board)
            else:
                comp_move = self.gp.find_best_move(board)
                if comp_move is None:
                    print("Gra zakończona, brak dostępnych ruchów.")
                    return
                if self.gp.insert_sign(board, comp_move[0], comp_move[1], 'O'):
                    print(f"\nKomputer wykonał ruch: wiersz {comp_move[0] + 1}, kolumna {comp_move[1] + 1}")
                    self.gp.print_board(board)
                    if self.gp.win_algorithm(board, 'O'):
                        print("\nKomputer wygrał!")
                        return
