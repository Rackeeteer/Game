board = list(range(1,10))
def display_board():
        print('1 2 3')
        print('-----')

def check_win(player):
    if (
        (board[1] == board[2] == board[3] == player) or
        (board[3] == board[4] == board[5] == player) or
        (board[6] == board[7] == board[8] == player) or
        (board[1] == board[3] == board[6] == player) or
        (board[1] == board[4] == board[7] == player) or
        (board[2] == board[5] == board[8] == player) or
        (board[1] == board[4] == board[9] == player) or
        (board[2] == board[4] == board[6] == player)
    ):
        return True
    else:
        return False

def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        position = int(input('Выберите позицию (1-9): '))

        if board[position - 1] == ' ':
            board[position - 1] = current_player

            if check_win(current_player):
                print('Игрок ' + current_player + ' выиграл!')
                game_over = True
            elif ' ' not in board:
                print('Ничья!')
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Данная позиция занята. Попробуйте снова.')
            play_game()
