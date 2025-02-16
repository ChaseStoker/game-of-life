import pygame


class GridEvolution:
    """Class to handle simulations on the grid"""
    def __init__(self, rows, cols, screen, block_size):
        self.screen = screen
        self.grid = [[False for _ in range(cols)] for _ in range(rows)]
        self.size = (rows, cols)
        self.block_size = block_size 


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
        pygame.draw.rect(screen, 'white', (x, y, self.block_size, self.block_size))



# pygame setup
pygame.init()
width, height = 1000, 1000
block_size = 10
cols =int(width/block_size)
rows = int(height/block_size)
tick_rate = 10

# Initialize game window
screen = pygame.display.set_mode((width, height))
screen_rect = screen.get_rect()
pygame.display.set_caption('Grid Evolution')
clock = pygame.time.Clock()

# Create game assets
grid = GridEvolution(rows, cols, screen, block_size)
running = True
simulation = False

sim_ind_font = pygame.font.Font(None, 30)
sim_ind_surf = sim_ind_font.render('Simulating', True, 'Green')
sim_ind_rect = sim_ind_surf.get_rect(topleft = (10, 10))


while running:
    screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            grid.update_cell(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulation = not simulation

    if simulation:
        grid.update_grid()
        screen.blit(sim_ind_surf, sim_ind_rect)

    grid.draw_grid()

    pygame.display.flip()
    clock.tick(tick_rate)

pygame.quit()




