import pygame as pg
import GameLogic

WIDTH = HEIGHT = 600
DIMENSIONS = 10
SQ_SIZE = HEIGHT // DIMENSIONS
IMAGES = {}

def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen.fill(pg.Color("white"))
    gs = GameLogic.GameState()  # gs - game-state
    load_images()
    running = True
    square_selected = ()
    selected_moves = []
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    gs.undo_move()
            elif event.type == pg.MOUSEBUTTONDOWN:
                click_coordinates = pg.mouse.get_pos()
                col = click_coordinates[0] // SQ_SIZE
                row = click_coordinates[1] // SQ_SIZE
                if square_selected == (row, col):
                    square_selected = ()
                    selected_moves = []
                elif (gs.board[row][col] in ["wp", "wk"]) and not gs.white_to_move:
                    square_selected = ()
                elif (gs.board[row][col] in ["bp", "bk"]) and gs.white_to_move:
                    square_selected = ()
                elif gs.board[row][col] == "--" and len(selected_moves) == 0:
                    square_selected = ()
                elif gs.board[row][col] != "--" and len(selected_moves) == 1:
                    square_selected = ()
                    selected_moves = []
                else:
                    square_selected = (row, col)
                    selected_moves.append(square_selected)
                if len(selected_moves) == 2 and gs.white_to_move and (selected_moves[0][0]-selected_moves[1][0] == 1 and selected_moves[0][1]-selected_moves[1][1] in [1, -1]):  # after the 2nd click
                    move = GameLogic.Move(selected_moves[0], selected_moves[1], gs.board)
                    gs.make_move(move)
                    square_selected = ()
                    selected_moves = []
                elif len(selected_moves) == 2 and not gs.white_to_move and (selected_moves[0][0]-selected_moves[1][0] == -1 and selected_moves[0][1]-selected_moves[1][1] in [1, -1]):
                    move = GameLogic.Move(selected_moves[0], selected_moves[1], gs.board)
                    gs.make_move(move)
                    square_selected = ()
                    selected_moves = []
                elif len(selected_moves) == 2:
                    square_selected = ()
                    selected_moves = []

        draw_game_state(screen, gs)
        pg.display.flip()

def load_images():
    pieces = ["wp", "wk", "bp", "bk"]
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)


def draw_board(screen):
    colors = [pg.Color("white"), pg.Color("purple")]
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


if __name__ == "__main__":
    main()
