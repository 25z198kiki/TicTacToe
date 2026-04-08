def new_board():
    return [" "] * 9


def print_board(board):
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print("\n")


def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def is_draw(board):
    return all(cell != " " for cell in board)


def make_move(board, position, player):
    if position < 0 or position > 8:
        raise ValueError("Position must be between 0 and 8")
    if board[position] != " ":
        raise ValueError("Cell is already occupied")
    board[position] = player


def play_game():
    board = new_board()
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter position (1-9): ")

        if not move.isdigit():
            print("Please enter a valid number.")
            continue

        position = int(move) - 1
        try:
            make_move(board, position, current_player)
        except ValueError as exc:
            print(exc)
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
