#
# Board.py  (Problem Set 10, Problem 1)
#
# A Connect Four Board class
#


class Board:
    choices = [1, 5, 10]
    goal = 20

    def __init__(self):
        self.pile = 0
        self.choices = Board.choices
        self.last_player = 0
        self.history = []

    def __repr__(self):
        # return " ".join([str(i) for i in self.history]) + "Total number: " + str(self.pile)
        return str(self.pile)

    def add_number(self, num, player):
        self.pile += num
        self.last_player = player

    def reset(self):
        '''reset the Board object on which it is called by
    setting all slots to contain a space character'''
        self.pile = 0
        self.last_player = 0

    def remove_number(self, num):
        '''removes the top checker from column
col of the called Board object. If the column is empty, then the method should do nothing'''
        self.pile -= num
        self.last_player = 1 - self.last_player

    def is_win_for(self, player):
        '''accepts a parameter checker that is
    either 'X' or 'O', and returns True if there are four consecutive slots containing checker
    on the board. Otherwise, it should return False.'''
        return (self.pile >= Board.goal and self.last_player == player)

            
                
        
        

