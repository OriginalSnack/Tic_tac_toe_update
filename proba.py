import math


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def is_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def evaluate(board):
    if is_winner(board, "X"):
        return 1
    if is_winner(board, "O"):
        return -1
    return 0


def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 1 or score == -1 or is_full(board):
        return score

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best_score = max(best_score, minimax(board, depth + 1, False))
                    board[i][j] = " "
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best_score = min(best_score, minimax(board, depth + 1, True))
                    board[i][j] = " "
        return best_score


def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O'. The computer is 'X'.")

    while True:
        print_board(board)

        # Player's move
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column: 0 1 2): ").split())
                if board[row][col] == " ":
                    board[row][col] = "O"
                    break
                else:
                    print("Cell is already occupied. Choose another one.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as two numbers between 0 and 2.")

        if is_winner(board, "O"):
            print_board(board)
            print("Congratulations, you win!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Computer's move
        print("Computer is making a move...")
        row, col = best_move(board)
        board[row][col] = "X"

        if is_winner(board, "X"):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()
