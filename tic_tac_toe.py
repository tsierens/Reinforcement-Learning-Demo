import numpy as np
import sys


def empty_board():
    return np.zeros(9)

def available_moves(board):
    moves=[]
    board = board.reshape(9)
    return [x for x in range(len(board)) if board[x] == 0]

def update_move(board, move, turn):
    board[move] = turn
    return None

def unupdate_move(board, move):
    board[move] = 0 
    return None

def all_rows(board):
    board = board.reshape((3,3))
    rows=[]
    for i in range(3):
        rows.append(board[i,:])
    for i in range(3):
        rows.append(board[:,i])
    rows.append(np.array([board[i,i] for i in range (3)]))
    rows.append(np.array([board[i,2-i] for i in range(3)]))
    return rows

def winner(board):
    for row in all_rows(board):
        if row[0]==row[1]==row[2]!=0:
            return row[0]
    return 0

def is_winner(board):
    return winner(board) != 0
def is_full(board):
    return np.prod(board) != 0


def is_over(board):
    return is_winner(board) or is_full(board)
    
def print_board(board):
    player_dict_r = {1:'X', -1:'O', 0: ' '}    
    print('''
   {} | {} | {}            1 | 2 | 3
   ----------          -----------
   {} | {} | {}            4 | 5 | 6
   ----------          -----------
   {} | {} | {}            7 | 8 | 9
    '''.format(player_dict_r[board.reshape(9)[0]],
               player_dict_r[board.reshape(9)[1]],
               player_dict_r[board.reshape(9)[2]],
               player_dict_r[board.reshape(9)[3]],
               player_dict_r[board.reshape(9)[4]],
               player_dict_r[board.reshape(9)[5]],
               player_dict_r[board.reshape(9)[6]],
               player_dict_r[board.reshape(9)[7]],
               player_dict_r[board.reshape(9)[8]],
              )
         )

class player:
    def make_move(self, board,active_turn):
        print( 'it is '+active_turn+'\'s turn, please choose a move')
        player_dict = {'X':1, 'O':-1}
        print_board(board)
        board = board.reshape(9)
        while True:
            move = raw_input()
            if move.isdigit():
                move = int(move)
            else:
                print('Please input an integer')
                continue
            if not (move in range(1,10)):
                print('Integer must be between 1 and 9')
                continue
            break
        return move
    
class result(object):
    def __init__(self,board,log):
        self.winner = winner(board)
        self.log = log
        self.board = board

def play(player_1,player_2):
    player_dict = {'X':1, 'O':-1}
    player_dict_r = {1:'X', -1:'O', 0: ' '}    
    swap_dict = {'O':'X','X':'O'}
    log=[]
    active_turn = 'X'
    board = empty_board()
    while not is_over(board):
        board = board.reshape(9)
        times_failed = 0
        while True:
            times_failed +=1
            if times_failed > 100:
                sys.exit('Failed to make a legal move 100 times.')
            if active_turn == 'X':
                move = player_1.make_move(board,active_turn)
            elif active_turn == 'O':
                move = player_2.make_move(board,active_turn)
            if board[move-1] == 0:
                board[move-1] = player_dict[active_turn]
                break
        log.append(move)
        active_turn = swap_dict[active_turn]
    '''
    if winner(board):
        print('The winner is ' + player_dict_r[int(winner(board))]+'!')
    else:
        print('Tie game!!!')
    '''
    return result(board,log)

