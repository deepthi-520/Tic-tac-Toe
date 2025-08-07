# Tic-Tac-Toe in Python

# Initialize the board
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'  # Player X starts

def initialize_board():
    global board
    board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("---|---|---")

def player_move():
    while True:
        try:
            row, col = map(int, input(f"Player {current_player}, enter your move (row and column 1-3): ").split())
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == ' ':
                board[row - 1][col - 1] = current_player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter two numbers separated by space (e.g., 1 2).")

def check_winner():
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == current_player for j in range(3)) or \
           all(board[j][i] == current_player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == current_player for i in range(3)) or \
       all(board[i][2 - i] == current_player for i in range(3)):
        return True

    return False

def is_draw():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Game loop
def play_game():
    global current_player
    initialize_board()
    winner = False

    while not winner and not is_draw():
        print_board()
        player_move()
        winner = check_winner()
        if not winner:
            current_player = 'O' if current_player == 'X' else 'X'

    print_board()
    if winner:
        print(f"Player {current_player} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()
