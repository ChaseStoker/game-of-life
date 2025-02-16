import pygame

class Grid:
    """Class to handle simulations on the grid"""
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.grid = [[False for _ in range(self.settings.cols)] for _ in range(self.settings.rows)]
        self.size = (self.settings.rows, self.settings.cols)
        self.block_size = self.settings.block_size 


    def update_cell(self, mouse_pos):
        x, y = mouse_pos
        col = x//self.block_size
        row = y//self.block_size
        self.grid[row][col] = not self.grid[row][col]


    def update_grid(self):
        rows, cols = self.size
        next_grid = [[False for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                num_neigbours = self._get_nn(row, col)
                CELL_ALIVE = self.grid[row][col]
                if CELL_ALIVE and num_neigbours in [2, 3]:
                    next_grid[row][col] = True
                elif not CELL_ALIVE and num_neigbours == 3:
                    next_grid[row][col] = True
        self.grid = next_grid


    def _get_nn(self, row, col):
        rows, cols = self.size
        nn = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = col + dx, row + dy
                if 0 <= nx < cols and 0 <= ny < rows:
                    nn += self.grid[ny][nx]
        return nn


    def draw_grid(self):
        rows, cols = self.size
        for row in range(rows):
            for col in range(cols):
                if self.grid[row][col]: 
                    self._draw_cell(row, col)


    def _draw_cell(self, row, col):
        y = row * self.block_size
        x = col * self.block_size
        pygame.draw.rect(self.screen, 'white', (x, y, self.block_size, self.block_size))