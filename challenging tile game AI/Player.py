#
# Player.py  (Problem Set 10, Problem 2)
#
# A Connect-Four Player class 
#  

from Board import Board

# write your class below

class Player():
    '''represents a player; consists of a checker'''
    def __init__(self, id):
        '''constructs a new player'''
        self.num_moves = 0
        self.id = id

    def __repr__(self):
        '''returns a string representing a Player object. The
string returned should indicate which checker the Player object is using'''
        return "Player " + self.id

    def opponent_id(self):
        '''returns a one-character string representing
the checker of the Player object’s opponent.'''
        return 1 - self.id

    def next_move(self, board):
        '''accepts a Board object as a
parameter and returns the column where the player wants to make the next move.'''
        num = int(input('Enter a number: '))
        try:
            assert(num in board.choices)
        except:
            print("Plz enter a value in " + board.choices + "!")
        self.num_moves += 1
        return num