import math

'''
    Klasa GamePlay ze wszystkimi funkcjami gry
'''


class GamePlay:
    '''
        Funkcja print_board() dla rysowania pola
     '''

    @classmethod
    def print_board(cls, board):
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

        for combination in list_wins:
            winning = True
            for row, col in combination:
                if board[row][col] != sign:
                    winning = False
                    break
            if winning:
                return True

    '''
        Funkcja insert_sign wstawia znaki do komórki,
        row - wiersz
        col - columna
    i'''

    @classmethod
    def insert_sign(cls, board, row, col, sign):
        if board[row][col] == ' ':
            board[row][col] = sign
            return True

    '''
        Funkcja check_win zwraca znak który, wygrał, 
        ona została tworzona specjalnie dla funkcji minimaks
    '''

    @classmethod
    def check_win(cls, board):
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            return board[0][2]
        return None

    '''
        Funkcja sprawdzająca czy są puste komórki
    '''

    @classmethod
    def is_move_left(cls, board):
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    return True
        return False

    '''
        Funkcja, która przedstawia algorytm minimaks:
        depth - głębokość 
        is_max - wartość boolean, domyślnie ustawiona na False. 
        Jeśli is_max jest False, oznacza to, że teraz ruch należy do komputera (maksymalizatora).
        Jeśli is_max jest True, oznacza to że teraz ruch należy do gracza(minimalizatora)'''

    @classmethod
    def minimax(slc, board, depth, is_max):
        winner = slc.check_win(board)
        if winner == '0':
            return 10 - depth
        if winner == 'X':
            return depth - 10
        if not slc.is_move_left(board):
            return 0

        if is_max:
            best = -math.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = 'X'
                        score = slc.minimax(board, depth + 1, False)
                        best = max(best, score)
                        board[row][col] = ' '
            return best
        else:
            best = math.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = 'O'
                        score = slc.minimax(board, depth + 1, True)
                        best = min(best, score)
                        board[row][col] = ' '
            return best

    '''
    ...
    '''

    @classmethod
    def find_move(slc, board):
        best_val = -math.inf
        best_move = None

        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    move_val = slc.minimax(board, 0, True)
                    board[row][col] = ' '

                    if move_val > best_val:
                        best_val = move_val
                        best_move = (row, col)
        return best_move
