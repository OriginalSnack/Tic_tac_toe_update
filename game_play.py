import math

'''
    Klasa GamePlay ze wszystkimi funkcjami gry
'''


class GamePlay:
    '''
        Funkcja print_board() dla rysowania pola
     '''

    @staticmethod
    def print_board(board):
        '''board to pole przedstawione jako lista z listów'''
        for i in range(3):
            row = []
            for j in range(3):
                row.append(board[i][j])
            print(" | ".join(row))
            if i < 2:
                print("---------")

    '''
        Funkcja win_algorithm  sprawdza kto wygrał
    '''

    @classmethod
    def win_algorithm(cls, board, sign):
        '''sign - znak gracza'''
        list_wins = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]

        for combinations in list_wins:
            if all(board[row][col] == sign for row, col in combinations):
                return True
        return False

    '''
        Funkcja insert_sign wstawia znaki do komórki,
        row - wiersz
        col - columna
    i'''

    @staticmethod
    def insert_sign(board, row, col, sign):
        if board[row][col] == ' ':
            board[row][col] = sign
            return True

    '''
        Funkcja sprawdzająca czy są puste komórki
    '''

    @staticmethod
    def is_full(board):
        return all(cell != " " for row in board for cell in row)

    @classmethod
    def evaluate(cls, board):
        if cls.win_algorithm(board, "O"):
            return 1
        elif cls.win_algorithm(board, "X"):
            return -1
        return 0

    '''
        Funkcja, która przedstawia algorytm minimaks:
        depth - głębokość 
        is_max - wartość boolean, domyślnie ustawiona na False. 
        Jeśli is_max jest False, oznacza to, że teraz ruch należy do komputera (maksymalizatora).
        Jeśli is_max jest True, oznacza to że teraz ruch należy do gracza(minimalizatora)'''

    @classmethod
    def minimax(cls, board, depth, is_max):
        score = cls.evaluate(board)

        if score == 1 or score == -1 or cls.is_full(board):
            return score

        if is_max:
            best_score = -math.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = "O"
                        best_score = max(best_score, cls.minimax(board, depth + 1, False))
                        board[row][col] = " "
            return best_score
        else:
            best_score = math.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = "X"
                        best_score = min(best_score, cls.minimax(board, depth + 1, True))
                        board[row][col] = " "
            return best_score

    '''
        Funkcja dla poszukiwania najliepszego chodu
    '''

    @classmethod
    def find_best_move(cls, board):
        best_score = -math.inf
        best_move = (-1, -1)

        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = cls.minimax(board, 0, False)
                    board[row][col] = " "

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        return best_move