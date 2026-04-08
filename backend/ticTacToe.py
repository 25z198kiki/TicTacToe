board = [" " for _ in range(9)]

def print_board():
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print("\n")
    

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def play_game():
    current_player = "X"
    turn = 0
    
    while turn < 9:
        print_board()
        move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
        
        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move! Try again.")
            continue  
        
        board[move] = current_player
        turn += 1  
        
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            return
        
        current_player = "O" if current_player == "X" else "X"
    
    print_board()
    print("It's a draw!")

play_game()