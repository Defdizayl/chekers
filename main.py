import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.board import Board
#from checkers.board import Board
from checkers.game import Game
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('checkers')
def get_row_get_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return  row, col
def main():
    run = True
    clock = pygame.time.Clock()
    #board = Board()
    game = Game(WIN)
    # piece = board.get_piece(0,1)
    # board.move(piece,4,3)
    while run:
        clock.tick(FPS)
        while game.winner() != None:
            print(game.winner())
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_get_col_from_mouse(pos)
                #piece = board.get_piece(row, col)
                #board.move(piece, 4, 3)
                game.select(row, col)

        #board.draw(WIN)
        #pygame.display.update()
        game.update()
    pygame.QUIT()
main()
