#-------GLOBAL VARIABLES-------

board = ["-","-","-",
         "-","-","-",
         "-","-","-"  ]

#if Game is still going
game_still_going = True

#who win or tie
winner = None

#who's turn is it

current_player = "X"

#display board
def display_board():

    print(board[0] + "|" + board[1] +"|"+board[2])
    print(board[3] + "|" + board[4] +"|"+board[5])
    print(board[6] + "|" + board[7] +"|"+board[8])

#start playing tic tac toe game
def play_game():    
    display_board()
    
    while game_still_going:
        
        #it handles the turn of players
        handle_turn(current_player)

        #check if game ended
        check_if_game_over()
        
        # Flip to next player
        flip_player()
    
    #the game has ended
    if winner == "X" or winner =="O":
        print(winner + " won")

    elif winner == None:
        print("Tie") 



def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position 1-9: ")

    valid = False

    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Go again")
    
    board[position] = player

    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    #setup global variable
    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else: 
        winner = None
    return

def check_rows():
    #setup global variables
    global game_still_going
    row_1 = board[0]==board[1]==board[2] !="-"
    row_2 = board[3]==board[4]==board[5] !="-"
    row_3 = board[6]==board[7]==board[8] !="-"

    # if any row does have a match, flag there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner, X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
     #setup global variables
    global game_still_going
    column_1 = board[0]==board[3]==board[6] !="-"
    column_2 = board[1]==board[4]==board[7]!="-"
    column_3 = board[2]==board[5]==board[8]!="-"

    # if any column does have a match, flag there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return the winner, X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
     #setup global variables
    global game_still_going
    diagonal_1 = board[0]==board[4]==board[8] !="-"
    diagonal_2 = board[6]==board[4]==board[2]!="-"
    

    # if any column does have a match, flag there is a win
    if diagonal_1 or diagonal_2 :
        game_still_going = False

    # Return the winner, X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

def flip_player():
    #global variables we need
    global current_player

    #if current player is X change it to O
    if current_player == "X":
        current_player = "O"
    #if current player is O change it to X
    elif current_player == "O":
        current_player = "X"

    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going =False
    return





if __name__=="__main__":
    play_game()


#board
#display board
#play game
#handle turn
#check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip player

