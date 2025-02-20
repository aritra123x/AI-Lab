import numpy as np
import random

def create_board():
    return np.zeros((3, 3), dtype=int)

def possibilities(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i, j] == 0]

def random_place(board, player):
    selection = possibilities(board)
    if selection:
        current_loc = random.choice(selection)
        board[current_loc] = player

def human_place(board):
    selection = possibilities(board)
    while True:
        try:
            row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
            if (row, col) in selection:
                board[row, col] = 1
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter two numbers between 0 and 2.")

def check_win(board, player):
    return any(
        all(board[i, j] == player for j in range(3)) or  
        all(board[j, i] == player for j in range(3)) for i in range(3)
    ) or all(board[i, i] == player for i in range(3)) or all(board[i, 2 - i] == player for i in range(3))

def evaluate(board):
    for player in [1, 2]:
        if check_win(board, player):
            return player
    return -1 if np.all(board != 0) else 0

def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    first_player = input("Do you want to play first? (y/n): ").strip().lower()
    human_turn = first_player == 'y'
    winner = 0
    
    while winner == 0:
        if human_turn:
            print("Your turn!")
            human_place(board)
        else:
            print("Computer's turn...")
            random_place(board, 2)
        
        print(board)
        winner = evaluate(board)
        human_turn = not human_turn
    
    if winner == 1:
        print("Congratulations! You win!")
    elif winner == 2:
        print("Computer wins. Better luck next time!")
    else:
        print("It's a tie!")

play_game()
