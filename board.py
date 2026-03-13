import copy

class MancalaBoard:

    def __init__(self):
        self.board = [4,4,4,4,4,4,0, 4,4,4,4,4,4,0]

    def clone(self):
        new = MancalaBoard()
        new.board = self.board.copy()
        return new

    def is_game_over(self):
        return sum(self.board[0:6]) == 0 or sum(self.board[7:13]) == 0

    def get_valid_moves(self, player):

        if player == 0:
            return [i for i in range(0,6) if self.board[i] > 0]
        else:
            return [i for i in range(7,13) if self.board[i] > 0]

    def make_move(self, pit, player):

        stones = self.board[pit]
        self.board[pit] = 0
        index = pit

        while stones > 0:

            index = (index + 1) % 14

            if player == 0 and index == 13:
                continue

            if player == 1 and index == 6:
                continue

            self.board[index] += 1
            stones -= 1

        return index

    def evaluate(self):

        return self.board[13] - self.board[6]