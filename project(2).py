board = ['_','_','_',
         '_','_','_',
         '_','_','_']
winner = None
current_player ='x'
def board_Display():
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

def Play_game():

    while True:

        board_Display()
        handle_turn()
        check_rows()
        check_columns()
        check_diaganols()
        swtich_player()
        if winner == 'x' or winner == 'o':
            board_Display()
            print(winner + '`s won.')
            break
        elif winner == None and '_' not in board:
            board_Display()
            print('tie.')
            break





def handle_turn():
        print(current_player +'`s turn.')
        position=int(input('enter a number between 1-9:'))-1
        while position > len(board)-1 or position <0:
            position = input('invalid number! choose number between 1-9:')
            position = int(position) - 1
        while board[position]  in ['x','o']:
                print('already taken')
                position = input('invalid number! choose number between 1-9:')
                position = int(position) -1

        board[position] = current_player








def check_rows():
    global winner
    row1 = board[0] == board[1] == board[2] != '_'
    row2 = board[3] == board[4] == board[5] != '_'
    row3 = board[6] == board[7] == board[8] != '_'
    if row1 or row2 or row3:
        winner = current_player
    return winner


def check_columns():
        global winner
        column1 = board[0] == board[3] == board[6] !='_'
        column2 = board[1] == board[4] == board[7] !='_'
        column3 = board[2] == board[5] == board[8] !='_'
        if column1 :
            winner = board[0]
        if column2 :
            winner = board[1]
        if column3 :
            winner = board[2]

def  check_diaganols():
        global winner
        diaganol1 = board[0] == board[4] == board[8] != '_'
        diaganol2 = board[2] == board[4] == board[6] != '_'
        if diaganol1 :
            winner = board[0]
        if diaganol2:
            winner = board[2]


def swtich_player():
        global current_player

        if current_player =='x' :
               current_player ='o'
        elif current_player == 'o' :
             current_player ='x'
        return current_player



def check_for_winner():

    check_diaganols()
    check_columns()
    check_rows()
    return



Play_game()
