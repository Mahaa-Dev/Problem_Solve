import random
random.seed()


def draw_board(board):
    # Draw the board
    print('---------')
    for row in board:
        print('|', end=' ')
        for item in row:
            print(item, end=' ')
        print('|')
    print('---------')


def welcome(board):
    # Print the welcome message and display the board
    print("Welcome to Tic-Tac-Toe!\n")
    draw_board(board)


def initialise_board(board):
    # Set all elements of the board to a space ' '
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board


def get_player_move(board):
    while True:
        move = int(
            input("Enter the number corresponding to the square you want:"))
        if move == 1:
            row = 0
            col = 0
        elif move == 2:
            row = 0
            col = 1
        elif move == 3:
            row = 0
            col = 2
        elif move == 4:
            row = 1
            col = 0
        elif move == 5:
            row = 1
            col = 1
        elif move == 6:
            row = 1
            col = 2
        elif move == 7:
            row = 2
            col = 0
        elif move == 8:
            row = 2
            col = 1
        elif move == 9:
            row = 2
            col = 2
        if board[row][col] == " ":
            return row, col
        print("This cell is already occupied. Try again.")


def choose_computer_move(board):
    # Let the computer choose a cell to put a nought in, return row and col
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            break
    return row, col


def check_for_win(board, mark):
    # Check if either the player or the computer has won, return True if someone won, False otherwise
    if (board[0][0] == board[1][1] == board[2][2] == mark) or \
       (board[0][2] == board[1][1] == board[2][0] == mark) or \
       (board[0][0] == board[0][1] == board[0][2] == mark) or \
       (board[1][0] == board[1][1] == board[1][2] == mark) or \
       (board[2][0] == board[2][1] == board[2][2] == mark) or \
       (board[0][0] == board[1][0] == board[2][0] == mark) or \
       (board[0][1] == board[1][1] == board[2][1] == mark) or \
       (board[0][2] == board[1][2] == board[2][2] == mark):
        return True
    return False


def check_for_draw(board):
    # Check if all cells are occupied, return True if it is, False otherwise
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def play_game(board):
    initialise_board(board)
    welcome(board)
    player = "X"
    computer = "O"
    while True:
        row, col = get_player_move(board)
        board[row][col] = player
        draw_board(board)
        if check_for_win(board, player):
            return 1
        if check_for_draw(board):
            return 0
        row, col = choose_computer_move(board)
        board[row][col] = computer
        draw_board(board)
        if check_for_win(board, computer):
            return -1
        if check_for_draw(board):
            return 0


def menu():
    while True:
        choice = input(
            "Enter 1 to play, 2 to save score, 3 to load scores, q to quit: ")
        if choice in ["1", "2", "3", "q"]:
            return choice
        print("Invalid choice, Try again.")


def load_scores():
    with open("leaderboard.txt", "r") as f:
        leaders = {}
        for line in f:
            name, score = line.strip().split(":")
            leaders[name] = int(score)
    return leaders


def save_score(score):
    name = input("Enter your name: ")
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}:{score}\n")


def display_leaderboard(leaders):
    print("Leaderboard:")
    for i, (player, score) in enumerate(sorted(leaders.items(), key=lambda x: x[1], reverse=True)):
        print(f"{i + 1}. {player}: {score}")
