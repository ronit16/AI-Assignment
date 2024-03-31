def print_board(board):
    print(" ")
    print(" ", board[0], " | ", board[1], " | ", board[2])
    print("----|----|----")
    print(" ", board[3], " | ", board[4], " | ", board[5])
    print("----|----|----")
    print(" ", board[6], " | ", board[7], " | ", board[8])
    print(" ")

def check_win(board, player):
    win = False
    if board[0] == board[1] == board[2] == player:
        win = True
    elif board[3] == board[4] == board[5] == player:
        win = True
    elif board[6] == board[7] == board[8] == player:
        win = True
    elif board[0] == board[3] == board[6] == player:
        win = True
    elif board[1] == board[4] == board[7] == player:
        win = True
    elif board[2] == board[5] == board[8] == player:
        win = True
    elif board[0] == board[4] == board[8] == player:
        win = True
    elif board[2] == board[4] == board[6] == player:
        win = True
    return win

def check_tie(board):
    tie = False
    if " " not in board:
        tie = True
    return tie

def minimax(board, player):
    if player == "O":
        best = [-1, -1000]
    else:
        best = [-1, 1000]
    if check_win(board, "X"):
        return [-1, -1]
    elif check_win(board, "O"):
        return [-1, 1]
    elif check_tie(board):
        return [-1, 0]
    for cell in range(0, 9):
        if board[cell] == " ":
            board[cell] = player
            score = minimax(board, "O" if player == "X" else "X")
            board[cell] = " "
            score[0] = cell
            if player == "O":
                if score[1] > best[1]:
                    best = score
            else:
                if score[1] < best[1]:
                    best = score
    return best

def opponent_turn(board):
    cell = int(input("Enter cell number: "))
    if board[cell] != " ":
        print("Invalid move")
        opponent_turn(board)
    else:
        board[cell] = "X"

def player_turn(board):
    cell = minimax(board, "O")[0]
    board[cell] = "O"

def main():
    board = [" " for i in range(9)]
    print_board(board)
    while True:
        opponent_turn(board)
        print_board(board)
        if check_win(board, "X"):
            print("Opponent wins")
            break
        if check_tie(board):
            print("It's a tie")
            break
        player_turn(board)
        print_board(board)
        if check_win(board, "O"):
            print("Player wins")
            break
        if check_tie(board):
            print("It's a tie")
            break

if __name__ == "__main__":
    main()