import pygame


class Game:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 600, 600
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.square_size = 300
        self.board = []
        self.create_board()

    def create_board(self):
        for row in range(0, 3):
            self.board.append([])
            for cell in range(0, 3):
                self.board[row].append('0')

    def move(self, row, col, x_y):
        self.board[row - 1][col - 1] = x_y.upper()

    def draw(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                pygame.draw.rect(self.win, (0, 0, 0),(row * self.square_size,
                                                      col * self.square_size,
                                                      self.square_size,
                                                      self.square_size))
