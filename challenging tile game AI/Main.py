#
# Main.py  (Problem Set 10, Problem 3)
#
# Playing the game 
#   

from Board import Board
from Player import Player
from AIPlayer import AIPlayer

def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.

    print('Welcome to THE GAME!')
    print()
    board = Board()
    print(board)
    
    while True:
        if process_move(player1, board) == True:
            return board

        if process_move(player2, board) == True:
            return board

def process_move(player, board):
    '''takes two parameters: a Player
object for the player whose move is being processed, and a Board object for the game that
is being played. The function will perform all of the steps involved in processing a single move by the
specified player on the specified board.'''
    print('Player ', player.id, '\'s turn: ', end="")

    num = player.next_move(board)


    board.add_number(num, player.id)
    print(board)
    if board.is_win_for(player.id) == True:
        print('player ', player.id, ' wins in ', player.num_moves, ' moves.\nCongratulations!')
        print(board.history)
        return True
    else:
        return False
    


player = Player(0)
aiPlayer = AIPlayer(1, 10)

board = connect_four(player, aiPlayer)
print(board)