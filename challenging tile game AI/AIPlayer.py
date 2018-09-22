#
# AIPlayer.py  (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from Board import Board
from Player import Player
import random

class AIPlayer(Player):
    '''this “AI player” will look ahead some number of moves into the future to assess the
impact of each possible move that it could make for its next move, and it will assign a score to
each possible move'''
    def __init__(self, id, lookahead):
        super().__init__(id)
        self.lookahead = lookahead

    def __repr__(self):
        return "AI Player " + self.id

    def max_score_column(self, scores):
        '''takes a list scores containing a
score for each column of the board, and that returns the index of the column with the
maximum score'''
        max_score = max(scores)

        score_indices = [i for i in range(len(scores)) if scores[i] == max_score]

        choices = [1, 5, 10]

        return choices[score_indices[0]]

    def scores_for(self, board):
        '''takes a Board object board and
determines the called AIPlayer‘s scores for the columns in board'''
        scores = [0] * len(board.choices)

        for i in range(len(scores)):
            if board.is_win_for(self.id):
                scores[i] = 100
            elif board.is_win_for(self.opponent_id()):
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                board.add_number(board.choices[i], self.id)

                opponent = AIPlayer(self.opponent_id(), self.lookahead - 1)
                max_opponent_score = max(opponent.scores_for(board))
                if (max_opponent_score == 100):
                    scores[i] = 0
                elif (max_opponent_score == 50):
                    scores[i] = 50
                elif (max_opponent_score == 0):
                    scores[i] = 100

                board.remove_number(board.choices[i])

        return scores

    def next_move(self, board):
        '''Rather than asking the user for the next move, this
version of next_move should return the called AIPlayer‘s judgment of its best possible
move.'''
        self.num_moves += 1
        scores = self.scores_for(board)
        return self.max_score_column(scores)