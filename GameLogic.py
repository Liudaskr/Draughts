class GameState:
    def __init__(self):
        self.board = [
            ["++", "bp", "++", "bp", "++", "bp", "++", "bp", "++", "bp"],
            ["bp", "++", "bp", "++", "bp", "++", "bp", "++", "bp", "++"],
            ["++", "bp", "++", "bp", "++", "bp", "++", "bp", "++", "bp"],
            ["bp", "++", "bp", "++", "bp", "++", "bp", "++", "bp", "++"],
            ["++", "--", "++", "--", "++", "--", "++", "--", "++", "--"],
            ["--", "++", "--", "++", "--", "++", "--", "++", "--", "++"],
            ["++", "wp", "++", "wp", "++", "wp", "++", "wp", "++", "wp"],
            ["wp", "++", "wp", "++", "wp", "++", "wp", "++", "wp", "++"],
            ["++", "wp", "++", "wp", "++", "wp", "++", "wp", "++", "wp"],
            ["wp", "++", "wp", "++", "wp", "++", "wp", "++", "wp", "++"]]

        self.white_to_move = True
        self.previous_moves = []

    def make_move(self, move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.previous_moves.append(move)
        self.white_to_move = not self.white_to_move

    def undo_move(self):
        if len(self.previous_moves) != 0:
            move = self.previous_moves.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move


class Move:
    def __init__(self, start_square, end_square, board):
        self.start_row = start_square[0]
        self.start_col = start_square[1]
        self.end_row = end_square[0]
        self.end_col = end_square[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
        self.moveID = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col
        print(self.moveID)

    def __eq__(self, other):
        return self.moveID == other.moveID

# need to place movement logic here
# possible moves must be placed in a list to check if an attempted move is possible
# if a capture is possible, all other basic moves must be ignored
