import pygame as pg
import copy
import random
import time

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
	
	def move(self, board):
		for r in range(10):
			for c in range(10):
				if gs.white_to_move is True:
					if board[r][c] == "wp":
						gs.check_captures(gs.board, r, c, move_list=None)
					if board[r][c] == "wk":
						gs.king_capture(gs.board, r, c, move_list=None)
				else:
					if board[r][c] == "bp":
						gs.check_captures(gs.board, r, c, move_list=None)
					if board[r][c] == "bk":
						gs.king_capture(gs.board, r, c, move_list=None)
		if len(CAPTURES) == 0:
			for r in range(10):
				for c in range(10):
					if gs.white_to_move is True:
						if board[r][c] == "wp":
							gs.check_white_moves(gs.board, r, c)
						if board[r][c] == "wk":
							gs.check_king_moves(gs.board, r, c)
					else:
						if board[r][c] == "bp":
							gs.check_black_moves(gs.board, r, c)
						if board[r][c] == "bk":
							gs.check_king_moves(gs.board, r, c)

	def check_captures(self, board, r, c, move_list):
		if gs.white_to_move is True:
			a, b, x, y, z = "bp", "bk", "bgp", "bgk", "wp"
		else:
			a, b, x, y, z = "wp", "wk", "wgp", "wgk", "bp"
		if move_list is None:
			move_list = []
		tempboard = board
		templist = move_list
		counter = 0
		templist.append(f"{r}{c}")
		if r > 1 and c < 8:
			if board[r-1][c+1] in [a, b] and board[r-2][c+2] == "--":
				tempboard[r][c] = "--"
				if tempboard[r-1][c+1] == a:
					tempboard[r-1][c+1] = x
				else:
					tempboard[r-1][c+1] = y
				tempboard[r-2][c+2] = z
				counter += 1
				gs.check_captures(tempboard, r-2, c+2, templist)
				tempboard[r][c] = z
				if tempboard[r-1][c+1] == x:
					tempboard[r-1][c+1] = a
				else:
					tempboard[r-1][c+1] = b
				tempboard[r-2][c+2] = "--"
		if r > 1 and c > 1:
			if board[r-1][c-1] in [a, b] and board[r-2][c-2] == "--":
				tempboard[r][c] = "--"
				if tempboard[r-1][c-1] == a:
					tempboard[r-1][c-1] = x
				else:
					tempboard[r-1][c-1] = y
				tempboard[r-2][c-2] = z
				counter += 1
				gs.check_captures(tempboard, r-2, c-2, templist)
				tempboard[r][c] = z
				if tempboard[r-1][c-1] == x:
					tempboard[r-1][c-1] = a
				else:
					tempboard[r-1][c-1] = b
				tempboard[r-2][c-2] = "--"
		if r < 8 and c > 1:
			if board[r+1][c-1] in [a, b] and board[r+2][c-2] == "--":
				tempboard[r][c] = "--"
				if tempboard[r+1][c-1] == a:
					tempboard[r+1][c-1] = x
				else:
					tempboard[r+1][c-1] = y
				tempboard[r+2][c-2] = z
				counter += 1
				gs.check_captures(tempboard, r+2, c-2, templist)
				tempboard[r][c] = z
				if tempboard[r+1][c-1] == x:
					tempboard[r+1][c-1] = a
				else:
					tempboard[r+1][c-1] = b
				tempboard[r+2][c-2] = "--"
		if r < 8 and c < 8:
			if board[r+1][c+1] in [a, b] and board[r+2][c+2] == "--":
				tempboard[r][c] = "--"
				if tempboard[r+1][c+1] == a:
					tempboard[r+1][c+1] = x
				else:
					tempboard[r+1][c+1] = y
				tempboard[r+2][c+2] = z
				counter += 1
				gs.check_captures(tempboard, r+2, c+2, templist)
				tempboard[r][c] = z
				if tempboard[r+1][c+1] == x:
					tempboard[r+1][c+1] = a
				else:
					tempboard[r+1][c+1] = b
				tempboard[r+2][c+2] = "--"
		if counter == 0 and len(templist) > 1:
			CAPTURES.append(copy.deepcopy(templist))
		return templist.pop()

	def check_white_moves(self, board, r, c):
		if r > 0 and c < 9 and board[r-1][c+1] == "--":
			MOVES.append(f"{r}{c}{r-1}{c+1}")
		if r > 0 and c > 0 and board[r-1][c-1] == "--":
			MOVES.append(f"{r}{c}{r-1}{c-1}")

	def check_king_moves(self, board, r, c):
		temp_r = r
		temp_c = c
		temp_r -= 1
		temp_c += 1
		while temp_r >= 0 and temp_c <= 9:
			if board[temp_r][temp_c] == "--":
				MOVES.append(f"{r}{c}{temp_r}{temp_c}")
				temp_r -= 1
				temp_c += 1
			else:
				break
		temp_r = r
		temp_c = c
		temp_r -= 1
		temp_c -= 1
		while temp_r >= 0 and temp_c >= 0:
			if board[temp_r][temp_c] == "--":
				MOVES.append(f"{r}{c}{temp_r}{temp_c}")
				temp_r -= 1
				temp_c -= 1
			else:
				break
		temp_r = r
		temp_c = c
		temp_r += 1
		temp_c -= 1
		while temp_r <= 9 and temp_c >= 0:
			if board[temp_r][temp_c] == "--":
				MOVES.append(f"{r}{c}{temp_r}{temp_c}")
				temp_r += 1
				temp_c -= 1
			else:
				break
		temp_r = r
		temp_c = c
		temp_r += 1
		temp_c += 1
		while temp_r <= 9 and temp_c <= 9:
			if board[temp_r][temp_c] == "--":
				MOVES.append(f"{r}{c}{temp_r}{temp_c}")
				temp_r += 1
				temp_c += 1
			else:
				break

	def check_black_moves(self, board, r, c):
		if r < 9 and c > 0 and board[r+1][c-1] == "--":
			MOVES.append(f"{r}{c}{r+1}{c-1}")
		if r < 9 and c < 9 and board[r+1][c+1] == "--":
			MOVES.append(f"{r}{c}{r+1}{c+1}")
	
	def make_the_move(self, moveID):
		if gs.white_to_move is True:
			piece, king = "wp", "wk"
		else:
			piece, king = "bp", "bk"
		if gs.board[int(moveID[0])][int(moveID[1])] == piece:
			gs.board[int(moveID[0])][int(moveID[1])] = "--"
			gs.board[int(moveID[2])][int(moveID[3])] = piece
		elif gs.board[int(moveID[0])][int(moveID[1])] == king:
			gs.board[int(moveID[0])][int(moveID[1])] = "--"
			gs.board[int(moveID[2])][int(moveID[3])] = king
		if gs.white_to_move is True and moveID[2] == "0":
			gs.board[int(moveID[2])][int(moveID[3])] = "wk"
		if gs.white_to_move is False and moveID[2] == "9":
			gs.board[int(moveID[2])][int(moveID[3])] = "bk"
		gs.white_to_move = not(gs.white_to_move)

	def make_the_capture(self, moveID):
		if gs.board[int(moveID[0])][int(moveID[1])] in ["wk", "bk"]:
			if gs.white_to_move is True:
				piece = "wk"
			else:
				piece = "bk"
			for i in range(len(moveID)-2)[::2]:
				gs.board[int(moveID[i])][int(moveID[i+1])] = "--"
				a = int(moveID[i])
				b = int(moveID[i+1])
				c = int(moveID[i+2])
				d = int(moveID[i+3])
				if a > c and b < d:
					for g, h in zip(range(10)[a-1:c:-1], range(10)[b+1:d]):
						if gs.board[g][h] != "--":
							gs.board[g][h] = "--"
				elif a > c and b > d:
					for g, h in zip(range(10)[a-1:c:-1], range(10)[b-1:d:-1]):
						if gs.board[g][h] != "--":
							gs.board[g][h] = "--"
				elif a < c and b > d:
					for g, h in zip(range(10)[a+1:c], range(10)[b-1:d:-1]):
						if gs.board[g][h] != "--":
							gs.board[g][h] = "--"
				elif a < c and b < d:
					for g, h in zip(range(10)[a+1:c], range(10)[b+1:d]):
						if gs.board[g][h] != "--":
							gs.board[g][h] = "--"
				gs.board[int(moveID[i+2])][int(moveID[i+3])] = piece
			gs.white_to_move = not(gs.white_to_move)
		else:
			if gs.white_to_move is True:
				piece = "wp"
			else:
				piece = "bp"
			for i in range(len(moveID)-2)[::2]:
				gs.board[int(moveID[i])][int(moveID[i+1])] = "--"
				gs.board[(int(moveID[i])+int(moveID[i+2]))//2][(int(moveID[i+1])+int(moveID[i+3]))//2] = "--"
				gs.board[int(moveID[i+2])][int(moveID[i+3])] = piece
			if gs.white_to_move is True and moveID[len(moveID)-2] == "0":
				gs.board[int(moveID[len(moveID)-2])][int(moveID[len(moveID)-1])] = "wk"
			if gs.white_to_move is False and moveID[len(moveID)-2] == "9":
				gs.board[int(moveID[len(moveID)-2])][int(moveID[len(moveID)-1])] = "bk"
			gs.white_to_move = not(gs.white_to_move)

	def king_capture(self, board, r, c, move_list):
		if gs.white_to_move is True:
			a, b, x, y, z = "bp", "bk", "bgp", "bgk", "wk"
		else:
			a, b, x, y, z = "wp", "wk", "wgp", "wgk", "bk"
		if move_list is None:
				move_list = []
		templist = move_list
		tempboard = copy.deepcopy(board)
		temp_r = r
		temp_c = c
		counter = 0
		templist.append(f"{r}{c}")
		while temp_r > 1 and temp_c < 8:
			if tempboard[temp_r-1][temp_c+1] in [a, b]:
				if tempboard[temp_r-2][temp_c+2] == "--":
					new_r = temp_r-2
					new_c = temp_c+2
					while new_r >= 0 and new_c <= 9 and tempboard[new_r][new_c] == "--":
						tempboard[r][c] = "--"
						if tempboard[temp_r-1][temp_c+1] == a:
							tempboard[temp_r-1][temp_c+1] = x
						else:
							tempboard[temp_r-1][temp_c+1] = y
						tempboard[new_r][new_c] = z
						gs.king_capture(tempboard, new_r, new_c, templist)
						counter += 1
						tempboard[r][c] = z
						if tempboard[temp_r-1][temp_c+1] == x:
							tempboard[temp_r-1][temp_c+1] = a
						else:
							tempboard[temp_r-1][temp_c+1] = b
						tempboard[new_r][new_c] = "--"
						new_r -= 1
						new_c += 1
					break
				else:
					break
			elif tempboard[temp_r-1][temp_c+1] == "--":
				temp_r -= 1
				temp_c += 1
			else:
				break
		temp_r = r
		temp_c = c

		while temp_r > 1 and temp_c > 1:
			if tempboard[temp_r-1][temp_c-1] in [a, b]:
				if tempboard[temp_r-2][temp_c-2] == "--":
					new_r = temp_r-2
					new_c = temp_c-2
					while new_r >= 0 and new_c >= 0 and tempboard[new_r][new_c] == "--":
						tempboard[r][c] = "--"
						if tempboard[temp_r-1][temp_c-1] == a:
							tempboard[temp_r-1][temp_c-1] = x
						else:
							tempboard[temp_r-1][temp_c-1] = y
						tempboard[new_r][new_c] = z
						gs.king_capture(tempboard, new_r, new_c, templist)
						counter +=1
						tempboard[r][c] = z
						if tempboard[temp_r-1][temp_c-1] == x:
							tempboard[temp_r-1][temp_c-1] = a
						else:
							tempboard[temp_r-1][temp_c-1] = b
						tempboard[new_r][new_c] = "--"
						new_r -= 1
						new_c -= 1
					break
				else:
					break
			elif tempboard[temp_r-1][temp_c-1] == "--":
				temp_r -= 1
				temp_c -= 1
			else:
				break
		temp_r = r
		temp_c = c

		while temp_r < 8 and temp_c > 1:
			if tempboard[temp_r+1][temp_c-1] in [a, b]:
				if tempboard[temp_r+2][temp_c-2] == "--":
					new_r = temp_r+2
					new_c = temp_c-2
					while new_r <= 9 and new_c >= 0 and tempboard[new_r][new_c] == "--":
						tempboard[r][c] = "--"
						if tempboard[temp_r+1][temp_c-1] == a:
							tempboard[temp_r+1][temp_c-1] = x
						else:
							tempboard[temp_r+1][temp_c-1] = y
						tempboard[new_r][new_c] = z
						gs.king_capture(tempboard, new_r, new_c, templist)
						counter +=1
						tempboard[r][c] = z
						if tempboard[temp_r+1][temp_c-1] == x:
							tempboard[temp_r+1][temp_c-1] = a
						else:
							tempboard[temp_r+1][temp_c-1] = b
						tempboard[new_r][new_c] = "--"
						new_r += 1
						new_c -= 1
					break
				else:
					break
			elif tempboard[temp_r+1][temp_c-1] == "--":
				temp_r += 1
				temp_c -= 1
			else:
				break
		temp_r = r
		temp_c = c

		while temp_r < 8 and temp_c < 8:
			if tempboard[temp_r+1][temp_c+1] in [a, b]:
				if tempboard[temp_r+2][temp_c+2] == "--":
					new_r = temp_r+2
					new_c = temp_c+2
					while new_r <= 9 and new_c <= 9 and tempboard[new_r][new_c] == "--":
						tempboard[r][c] = "--"
						if tempboard[temp_r+1][temp_c+1] == a:
							tempboard[temp_r+1][temp_c+1] = x
						else:
							tempboard[temp_r+1][temp_c+1] = y
						tempboard[new_r][new_c] = z
						gs.king_capture(tempboard, new_r, new_c, templist)
						counter +=1
						tempboard[r][c] = z
						if tempboard[temp_r+1][temp_c+1] == x:
							tempboard[temp_r+1][temp_c+1] = a
						else:
							tempboard[temp_r+1][temp_c+1] = b
						tempboard[new_r][new_c] = "--"
						new_r += 1
						new_c += 1
					break
				else:
					break
			elif tempboard[temp_r+1][temp_c+1] == "--":
				temp_r += 1
				temp_c += 1
			else:
				break
		temp_r = r
		temp_c = c

		if counter == 0 and len(templist) > 1:
			CAPTURES.append(copy.deepcopy(templist))
		return templist.pop()


WIDTH = HEIGHT = 800
DIMENSIONS = 10
SQ_SIZE = HEIGHT // DIMENSIONS
IMAGES = {}
CAPTURES = []
MOVES = []


def load_images():
	for piece in ["wp", "wk", "bp", "bk"]:
		IMAGES[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

gs = GameState()

def main():
	templist = []
	pg.init()
	screen = pg.display.set_mode((WIDTH, HEIGHT))
	screen.fill(pg.Color("white"))
	load_images()
	game_going = True
	while game_going:
		global CAPTURES
		CAPTURES = []
		global MOVES
		MOVES = []
		draw_game_state(screen, gs)
		pg.display.flip()
		running = True
		gs.move(gs.board)
		if CAPTURES:
			CAPTURES = ["".join(x) for x in CAPTURES if max([len(x) for x in CAPTURES]) == len(x)]
			temp_moves = copy.deepcopy(CAPTURES)
			#if gs.white_to_move is False:
			time.sleep(1)
			gs.make_the_capture(random.choice(CAPTURES))
			running = False
		elif MOVES:
			temp_moves = copy.deepcopy(MOVES)
			#if gs.white_to_move is False:
			time.sleep(1)
			gs.make_the_move(random.choice(MOVES))
			running = False
		else:
			if gs.white_to_move is True:
				print("Black wins!")
				running = False
				game_going = False
			else:
				print("White wins!")
				running = False
				game_going = False
		while running:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					running = False
					game_going = False
				elif event.type == pg.MOUSEBUTTONDOWN:
					click_coordinates = pg.mouse.get_pos()
					col = click_coordinates[0] // SQ_SIZE
					row = click_coordinates[1] // SQ_SIZE
					templist.append(f"{row}{col}")
					counter = 0
					temp_temp_moves = []
					if CAPTURES:
						for move in temp_moves:
							if move[len(templist)*2-2:len(templist)*2] == templist[len(templist)-1]:
								counter += 1
								temp_temp_moves.append(move)
						if len(temp_temp_moves) == 1:
							gs.make_the_capture(temp_temp_moves[0])
							templist = []
							running = False
						elif counter == 0:
							templist = []
							temp_moves = copy.deepcopy(CAPTURES)
							draw_game_state(screen, gs)
						else:
							temp_moves = copy.deepcopy(temp_temp_moves)
							draw_clicked_square(screen, row, col)
					else:
						for move in temp_moves:
							if move[len(templist)*2-2:len(templist)*2] == templist[len(templist)-1]:
								counter += 1
								temp_temp_moves.append(move)
						if len(temp_temp_moves) == 1:
							gs.make_the_move(temp_temp_moves[0])
							templist = []
							running = False
						elif counter == 0:
							templist = []
							temp_moves = copy.deepcopy(MOVES)
							draw_game_state(screen, gs)
						else:
							temp_moves = copy.deepcopy(temp_temp_moves)
							draw_clicked_square(screen, row, col)
						

def draw_game_state(screen, gs):
	draw_board(screen)
	draw_pieces(screen, gs.board)


def draw_board(screen):
	colors = [pg.Color("bisque2"), pg.Color("burlywood4")]
	for r in range(DIMENSIONS):
		for c in range(DIMENSIONS):
			color = colors[((r + c) % 2)]
			pg.draw.rect(screen, color, pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board):
	for r in range(DIMENSIONS):
		for c in range(DIMENSIONS):
			piece = board[r][c]
			if piece not in ["--", "++"]:
				screen.blit(IMAGES[piece], pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_clicked_square(screen, r, c):
	pg.draw.rect(screen, pg.Color("salmon4"), pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
	if gs.board[r][c] not in ["--", "++"]:
		screen.blit(IMAGES[gs.board[r][c]], pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
	pg.display.flip()


if __name__ == "__main__":
	main()
