import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def get_free_squares(board):
    free = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == " ":
                free.append([x,y])
    return free


def make_random_move(board,mark):
    free = get_free_squares(board)
    ai_move = free[int(len(free) * random.random())]
    board[ai_move[0]][ai_move[1]] = mark
    return board
    
def better_move(board,mark):
    free = get_free_squares(board)
    for i in free:
        board[i[0]][i[1]] = mark
        if is_win(board,mark):
            return board
        board[i[0]][i[1]] = " "

    rand = free[int(len(free) * random.random())]
    board[rand[0]][rand[1]] = mark

    return board


def is_row_all_marks(board,mark):
    for i in board:
        if i[0]==mark and i[1] == mark and i[2] == mark:
            return True
    return False
def is_col_all_marks(board,mark):
    for i in range(3):
        if board[0][i]==mark and board[1][i] == mark and board[2][i] == mark:
            return True
    return False
def is_diag(board,mark):
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[2][0] == mark and board[1][1] == mark and board[0][2] == mark:
        return True
    return False
def is_win(board,mark):
    return is_row_all_marks(board,mark) or is_col_all_marks(board,mark) or is_diag(board,mark)


if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    

    print("START GAME\n")
    turn = "X"
    while True:
        turn = "X"
        move = int(input("\nEnter your move: "))-1
        board[move//3][move%3] = "X"
        print_board_and_legend(board)
        
        if is_win(board,turn):
            break
        
        print("\nAI TURN\n")
        turn = "O"
        board = make_random_move(board,turn)
        print_board_and_legend(board)    

        if is_win(board,turn):
            break

    print("\n\n",turn," WON THE GAME!!")
    print("=============")
    print_board_and_legend(board)
    print("=============")
