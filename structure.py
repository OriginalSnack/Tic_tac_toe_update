class GamePlay:
    @classmethod
    def print_board(cls, sign_dict):
        for i in range(3):
            row = []
            for j in range(3):
                row.append(sign_dict[i][j])
            print(" | ".join(row))
            if i < 2:
                print("---------")

    @classmethod
    def win_algorithm(cls, sign_dict, sign):
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
                if sign_dict[row][col] != sign:
                    winning = False
                    break
            if winning:
                return True

    # for inserting signs in cells
    @classmethod
    def insert_sign(cls, board, row, col, sign):
        row_new = row - 1
        col_new = col - 1
        if board[row_new][col_new] == ' ':
            board[row_new][col_new] = sign
            return True

    @classmethod
    def evaluate(cls, board):
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2]:
                if board[row][0] == 'X':
                    return 10  # виграш компютера
                elif board[row][0] == 'O':
                    return -10  # програш для компютера

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col]:
                if board[0][col] == 'X':
                    return 10  # виграш компютера
                elif board[0][col] == 'O':
                    return -10  # програш для компютера

        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'X':
                return 10  # виграш компютера
            elif board[0][0] == 'O':
                return -10  # програш для компютера

        if board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == 'X':
                return 10  # виграш компютера
            elif board[0][2] == 'O':
                return -10  # програш для компютера
        return 0

    @classmethod
    def is_move_left(cls, board):
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    return True
        return False

    @classmethod
    def minimax(slc, board, depth, is_max):
        score = slc.evaluate(board)
        if score == 10:
            return score - depth
        if score == -10:
            return score + depth

        if not slc.is_move_left(board):
            return 0

        if is_max:
            best = -1000
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = 'X'
                        best = max(best, slc.minimax(board, depth + 1, is_max))
                        board[row][col] = ' '
            return best
        else:
            best = 1000
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = 'O'
                        best = min(best, slc.minimax(board, depth + 1, not is_max))
                        board[row][col] = ' '
            return best

    @classmethod
    def find_move(slc, board):
        best_val = -1000
        best_move = (-1, -1)

        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    move_val = slc.minimax(board, 0, False)
                    board[row][col] = ' '

                    if move_val > best_val:
                        best_move = (row, col)
                        best_val = move_val
        return best_move

