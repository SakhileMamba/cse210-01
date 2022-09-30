def check_win(board):

    if ((board[1] == board[2] and board[2] == board[3]) or
            (board[4] == board[5] and board[5] == board[6]) or
            (board[7] == board[8] and board[8] == board[9]) or
        (board[1] == board[4] and board[4] == board[7]) or
                (board[2] == board[5] and board[5] == board[8]) or
            (board[3] == board[6] and board[6] == board[9]) or
            (board[1] == board[5] and board[5] == board[9])
        ):
        return True
    else:
        return False


def board_state(board):
    return f'''
                    {board[1]}|{board[2]}|{board[3]}
                    -+-+-
                    {board[4]}|{board[5]}|{board[6]}
                    -+-+-
                    {board[7]}|{board[8]}|{board[9]}
                '''


def main():

    total_game_moves = 0
    board = {1: "1", 2: "2", 3: "3", 4: "4",
             5: "5", 6: "6", 7: "7", 8: "8", 9: "9", }

    player1 = "x"
    player2 = "o"

    print("PLAY TIC-TAC-TOE\n")
    print(f"Player one {player1} is your avatar.")
    print(f"Player two {player2} is your avatar.\n")

    print(board_state(board))

    last_move = "x"
    while total_game_moves < 9 and not (check_win(board)):
        if last_move == "o":
            input_move = True
            while input_move:
                try:
                    player1_move = int(
                        input("Player one please enter your move: "))
                    input_move = False
                    total_game_moves += 1
                    last_move = "x"
                except:
                    print("Please enter a valid number between 1 and 9")

            if (player1_move >= 1 and player1_move <= 9):
                if board[player1_move] == str(player1_move):
                    board[player1_move] = player1
                else:
                    print(
                        "Sorry you cannot make this move, this square is already taken.")

            print(f'''
                    {board[1]}|{board[2]}|{board[3]}
                    -+-+-
                    {board[4]}|{board[5]}|{board[6]}
                    -+-+-
                    {board[7]}|{board[8]}|{board[9]}
                ''')
        else:
            input_move = True
            while input_move:
                try:
                    player2_move = int(
                        input("Player two please enter your move: "))
                    input_move = False
                    total_game_moves += 1
                    last_move = "o"
                except:
                    print("Please enter a valid number between 1 and 9")

            if (player2_move >= 1 and player2_move <= 9):
                if board[player2_move] == str(player2_move):
                    board[player2_move] = player2
                else:
                    print(
                        "Sorry you cannot make this move, this square is already taken.")

            print(f'''
                    {board[1]}|{board[2]}|{board[3]}
                    -+-+-
                    {board[4]}|{board[5]}|{board[6]}
                    -+-+-
                    {board[7]}|{board[8]}|{board[9]}
                ''')

    if (check_win(board)):
        print(f"Congratulations {last_move}, You have won the game")
    else:
        print("The game has ended in a draw")


if __name__ == "__main__":
    main()
