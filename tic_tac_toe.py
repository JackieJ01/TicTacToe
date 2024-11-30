import random

# Initialize the board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check if a move is valid
def is_valid_move(board, row, col):
    return board[row][col] == ' '

# Make a move
def make_move(board, row, col, player):
    board[row][col] = player

# Check for a win
def check_winner(board):
    # Rows, columns, and diagonals
    lines = board + [list(col) for col in zip(*board)] + [
        [board[i][i] for i in range(3)],
        [board[i][2 - i] for i in range(3)],
    ]
    if ['X'] * 3 in lines:
        return 'X'
    elif ['O'] * 3 in lines:
        return 'O'
    return None

# Check for a draw
def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Evaluate the board for minimax
def evaluate(board):
    winner = check_winner(board)
    if winner == 'X':
        return -10
    elif winner == 'O':
        return 10
    return 0

# Minimax with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    winner = check_winner(board)
    if winner or is_draw(board) or depth == 0:
        return evaluate(board)
    
    if maximizing_player:
        max_eval = float('-inf')
        for row in range(3):
            for col in range(3):
                if is_valid_move(board, row, col):
                    board[row][col] = 'O'
                    eval = minimax(board, depth - 1, alpha, beta, False)
                    board[row][col] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if is_valid_move(board, row, col):
                    board[row][col] = 'X'
                    eval = minimax(board, depth - 1, alpha, beta, True)
                    board[row][col] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Get the best move for AI
def get_best_move(board):
    best_value = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if is_valid_move(board, row, col):
                board[row][col] = 'O'
                move_value = minimax(board, 3, float('-inf'), float('inf'), False)
                board[row][col] = ' '
                if move_value > best_value:
                    best_value = move_value
                    best_move = (row, col)
    return best_move

# Main game loop
def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    board = create_board()
    human = 'X'
    ai = 'O'
    print_board(board)

    while True:
        # Human's turn
        print("Your turn (X). Enter row and column (0-2): ")
        while True:
            try:
                row, col = map(int, input().split())
                if is_valid_move(board, row, col):
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Enter valid integers for row and column.")
        make_move(board, row, col, human)
        print_board(board)
        if check_winner(board):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI's turn
        print("AI's turn (O):")
        row, col = get_best_move(board)
        if row is not None and col is not None:
            make_move(board, row, col, ai)
        print_board(board)
        if check_winner(board):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
