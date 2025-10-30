import random
from random import randint

num_ships = 5
water = '~'
ship = 's'
sunk_ship = 'X'
wrong_guess = '.'

computer_board = [[water] * 10 for _ in range(10)]
player_board = [[water] * 10 for _ in range(10)]

chars = "ABCDEFGHIJ"

def print_player_board(board):
    print("   A B C D E F G H I J")
    for i, row in enumerate(board):
        print(f"{i + 1}  {' '.join(row)}")
        
        
def shows_computer_board(board):
     print(f'  A B C D E F G H I J')
     print(f'_____________________')
     
     for i, row in enumerate(board):

        print(f"{i + 1} ",end="")
        
        for j in range(len(row)):
            if row[j] == sunk_ship:
                print(f"{sunk_ship} ", end="")
                
            elif row[j] == wrong_guess:
                print(f"{wrong_guess} ", end="", )
                 
            elif row[j] == ship:
                print(f"{ship} ", end="")

            else:
                print(f"{water} ", end="")
                
        print("")
            
def shows_hidden_computer_board(board):
    print(f'  A B C D E F G H I J')
    print(f'_____________________')

    for i, row in enumerate(board):
        print(f"{i + 1} ",end="")
        for j in range(len(row)):
            if row[j] == sunk_ship:
                print(f"{sunk_ship} ", end="")
            elif row[j] == wrong_guess:
                print(f"{wrong_guess} ", end="", )
            else:
                print(f"{water} ", end="")
        
        print("")

def count_sunk_ships(board):
    return sum(row.count(sunk_ship) for row in board)

def show_info(player_board, computer_board):
    print(f"Remaining ally ships: {num_ships - count_sunk_ships(player_board)}")
    print(f"Remaining opponent ships: {num_ships - count_sunk_ships(computer_board)}")
    print("Computer board:")

def build_computer_board(board):
    for _ in range(num_ships):
        while True:
            r, c = random.randint(0, 9), random.randint(0, 9)
            if board[r][c] == ship:
                continue
            board[r][c] = ship
            break
    return board


def position_ships(board):
    print("\n Place your 5 ships ")
    chars = "ABCDEFGHIJ"

    for i in range(num_ships):
        while True:
            print_player_board(player_board)
            print(f"\nPlacing ship {i + 1}/{num_ships}")
            row_input = input("Enter the row (1-10): ")

            if not row_input.isdigit():
                print("Invalid row. Please enter a number between 1 and 10.")
                continue

            row = int(row_input) - 1

            if not (0 <= row <= 9):
                print("Position out of range. Row must be between 1 and 10. Try again")
                continue
            col_input = input("Enter the column (A-J): ").upper()

            if col_input not in chars:
                print("Invalid column. Please enter a letter between A and J")
                continue

            col = chars.index(col_input)
            if board[row][col] == ship:
                print(" This position is already occupied. Try again")
                continue
            board[row][col] = ship
            print(f"Ship {i + 1} placed at {col_input}{row_input}.")
            break

    print("\nYour board is ready!")
    print_player_board(board)
    return board


def battleship(player_board, computer_board):
    player_board = position_ships(player_board)
    computer_board = build_computer_board(computer_board)
    player_turn = True

    while True:
            player_ships = num_ships - count_sunk_ships(player_board)
            computer_ships = num_ships - count_sunk_ships(computer_board)

            if computer_ships == 0:
                print("You have won the game")
                break
            if player_ships == 0:
                print("You have lost the game")
                break

            if player_turn:
                print("Your turn")

                print("Options: 1 - Peek at enemy censored board | 2 - Attack | 3 - Peek at enemy board ")
                opt_input = input("Choose an option: ")

                if not opt_input.isdigit():
                    print("Invalid option. Please enter 1, 2 or 3")
                    continue

                opt = int(opt_input)

                if opt == 1:
                    show_info(player_board, computer_board)
                    shows_hidden_computer_board(computer_board)
                    continue
                
                elif opt == 3:
                    shows_computer_board(computer_board)
                    
                elif opt != 2:
                    print("Invalid option. Please enter 1, 2 or 3")
                    continue

                while True:

                    row_input = input("Enter enemy row (1-10): ")
                    col_input = input("Enter enemy column (A-J): ").upper()
                    chars = "ABCDEFGHIJ"

                    if not row_input.isdigit():
                        print("Invalid row input. Please enter a number (1-10).")
                        continue

                    row = int(row_input) - 1

                    if col_input not in chars:
                        print("Invalid column input. Please enter a letter (A-J).")
                        continue

                    col = chars.index(col_input)

                    if not (0 <= row <= 9 and 0 <= col <= 9):
                        print("Invalid coordinates. Row or Column out of bounds. Try again.")
                        continue

                    if computer_board[row][col] in (sunk_ship, wrong_guess):
                        print("Position already attacked. Choose another")
                        continue

                    break

                if computer_board[row][col] == ship:
                    print("You hit the enemy ship")
                    computer_board[row][col] = sunk_ship
                    continue
                else:
                    print("You hit the sea")
                    computer_board[row][col] = wrong_guess
                    player_turn = False
            else:
                print("Enemy's turn...")
                from random import randint

                row, col = randint(0, 9), randint(0, 9)
                while player_board[row][col] == sunk_ship or player_board[row][col] == wrong_guess:
                    row, col = randint(0, 9), randint(0, 9)

                if player_board[row][col] == ship:
                    print("Enemy hit your ship")
                    player_board[row][col] = sunk_ship
                else:
                    print("Enemy hit the sea")
                    player_board[row][col] = wrong_guess
                    player_turn = True

            show_info(player_board, computer_board)

if __name__ == "__main__":
    computer_board = [[water] * 10 for _ in range(10)]
    player_board = [[water] * 10 for _ in range(10)]
    battleship(player_board, computer_board)
