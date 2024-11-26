from game_play import GamePlay
from computer import Machine

# instrukcja
instructions = """To będzie nasza plansza do gry w kółko i krzyżyk (tic tac toe)

 (1 1) | (1 2) | (1 3) 
-------|-------|------
 (2 1) | (2 2) | (2 3) 
-------|-------|------
 (3 1) | (3 2) | (3 3) 

*instrukcje:

1. Masz wybór: grać z komputerom ałbo z kolegą.
2. Wprowadź parę liczb (x-wiersz, y-kolumnę),aby umieścić swój znak.
3. Musisz wypełnić wszystkie pola, aby uzyskać wynik.
4. Gracz 1 zaczyna pierwszy.
"""

# обєкт класу Gameplay()
gp = GamePlay()


def game_with_human(board):
    # дошкa
    player1 = input(f"\nWpisz imię pierwszego gracza: ")
    player2 = input("Wpisz imię drugiego gracza: ")
    players = [player1, player2]
    znaky = ['X', 'O']

    for i in range(9):
        curent_player = players[i % 2]
        curent_sign = znaky[i % 2]
        while True:
            try:
                row, col = map(int, input(
                    f"\n{curent_player}, wprowadź współrzędne (wiersz i kolumna) oddzielone spacją: ").split())
                if gp.insert_sign(board, row-1, col-1, curent_sign):
                    gp.print_board(board)
                    if gp.win_algorithm(board, curent_sign):
                        print(f"\n{curent_player} wygrał!")
                        return
                    break
                else:
                    print("Pole zajęte, spróbuj ponownie.")
            except ValueError:
                print("Nieprawidłowe współrzędne, wprowadź liczby.")

    print("\nRemis")


# Основна функція запуску
def main():
    sign_dict = [[' ' for _ in range(3)] for _ in range(3)]
    print(instructions)
    while (True):
        try:
            choise = int(input(f"\nTryb gry 1 (z osobą) lub 2 (z komputerem): "))
            if choise == 1:
                game_with_human(sign_dict)
                break
            elif choise == 2:
                print("Tryb gry z komputerem jest w trakcie opracowywania...")
                player12 = input("Podaj swoje imię: ")
                level_game = input("Wprowadź poziom trudności: 1(łatwy) lub 2(trudny): ")
                si = Machine(player12, 'O')
                if level_game == 1:
                    si.first_level_game(sign_dict)
                else:
                    si.second_level_game(sign_dict)
                break
            else:
                print("Nieprawidłowe dane, spróbuj ponownie")
        except ValueError:
            print("Nieprawidłowe dane, spróbuj ponownie")


if __name__ == "__main__":
    main()
