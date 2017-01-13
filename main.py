import pygame
from board import Board

pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

window_size = (600, 600)
screen = pygame.display.set_mode(window_size)

clock = pygame.time.Clock()

if __name__ == '__main__':
    board = Board(screen)
    player = 2
    moves = 9
    while True:
        screen.fill(BLACK)
        board.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                row, line = pygame.mouse.get_pos()
                line //= 200
                row //= 200
                if board.check(row, line) == 'can be placed here':
                    if player == 1:
                        player = 2
                    elif player == 2:
                        player = 1
                    board.color(player, line, row)
                    moves -= 1
        if board.check_win(1) == 'win':
            screen.fill(BLUE)
            pygame.display.flip()
            pygame.time.wait(1000)
            board.reset()
        elif board.check_win(2) == 'win':
            screen.fill(GREEN)
            pygame.display.flip()
            pygame.time.wait(1000)
            board.reset()
        if moves == 0:
            moves = 9
            board.reset()
        pygame.display.flip()