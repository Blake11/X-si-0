import pygame


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class Board(object):
    matrice = [[0 for i in range(3)] for j in range(3)]
    def __init__(self,screen):
        self.screen = screen

    def reset(self):
        self.matrice = [[0 for i in range(3)] for j in range(3)]

    def check_lines(self, player):
        for lines in self.matrice:
            if lines == [player]*3:
                return 'win'
        return 'not yet'

    def check_rows(self, player):
        for j in range(len(self.matrice)):
            ok = True
            for i in range(len(self.matrice)):
                if self.matrice[i][j] != player:
                    ok = False
            if ok:
                return 'win'
        return 'not yet'

    def check_main_diag(self, player):
        for i in range(len(self.matrice)):
            if self.matrice[i][i] != player:
                return 'not yet'
        return 'win'

    def check_second_diag(self, player):
        for i in range(len(self.matrice)):
            if self.matrice[len(self.matrice)-1-i][i] != player:
                return 'not yet'
        return 'win'

    def check_win(self, player):
        if self.check_lines(player) == 'win'\
                or self.check_rows(player) == 'win'\
                or self.check_main_diag(player) == 'win'\
                or self.check_second_diag(player) == 'win':
            return 'win'
        else:
            return 'not yet'

    def check(self, line, row):
        if self.matrice[line][row] != 0:
            return 'can’t place here'
        else:
            return 'can be placed here'

    def draw(self):
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice)):
                if self.matrice[i][j] == 0:
                    pygame.draw.rect(self.screen, WHITE, (i * 200, j * 200, 200, 200))
                elif self.matrice[i][j] == 1:
                    pygame.draw.rect(self.screen, BLUE, (i * 200, j * 200, 200, 200))
                elif self.matrice[i][j] == 2:
                    pygame.draw.rect(self.screen, GREEN, (i * 200, j * 200, 200, 200))

    def color(self, player, line, row):
        self.matrice[row][line] = player
