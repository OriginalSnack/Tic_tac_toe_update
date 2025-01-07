from game_play import GamePlay
from computer import Machine

# instrukcja
instrukcja = """To będzie nasza plansza do gry w kółko i krzyżyk (tic tac toe)

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

'''
    Funkcja, która pozwala grać z kolegą
'''


def game_with_human():
    # object klasu GamePlay
    gp = GamePlay()
    board = [[' ' for _ in range(3)] for _ in range(3)]

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
                if 1 <= row <= 3 and 1 <= col <= 3:
                    if gp.insert_sign(board, row - 1, col - 1, curent_sign):
                        gp.print_board(board)
                        if gp.win_algorithm(board, curent_sign):
                            print(f"\n{curent_player} wygrał!")
                            return
                        break
                    else:
                        print("Pole zajęte, spróbuj ponownie.")
                else:
                    print("Wprowadź liczby od 1 do 3.")
            except (IndexError, ValueError):
                print("Nieprawidłowe współrzędne, wprowadź liczby.")
    print("\nRemis")


def start_new_game(user_input: str):
    user_input = user_input.strip().lower()
    if user_input == "tak":
        return True
    elif user_input == "nie":
        return False
    else:
        print("Invalid choice")
        raise ValueError


def main():
    print(instrukcja)
    is_game_finished = True
    while is_game_finished == True:
        try:
            choice = int(input(f"\nTryb gry 1 (z osobą) lub 2 (z komputerem): "))
            if choice == 1:
                game_with_human()
            elif choice == 2:
                player12 = input("Podaj swoje imię: ")
                level_game = int(input("Wprowadź poziom trudności: 1(łatwy) lub 2(trudny): "))
                si = Machine(player12, 'O')
                if level_game == 1:
                    si.first_level_game()
                elif level_game == 2:
                    si.second_level_game()
                else:
                    print("Nieprawidłowe dane, spróbuj ponownie")
                    continue
            else:
                print("Nieprawidłowe dane, spróbuj ponownie")
        except ValueError:
            print("Nieprawidłowe dane, spróbuj ponownie")

        new_game_input = input(f"\n Chcesz zagrać jeszcze raz? tak lub nie: ")
        is_game_finished = True if start_new_game(new_game_input) else False


if __name__ == "__main__":
    main()
