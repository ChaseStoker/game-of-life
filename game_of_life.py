import pygame
from settings import Settings
from grid import Grid


class GameOfLife:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.running = True
        self.simulation = False
        self.spawning = False
        self.killing = False

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Grid Evolution')

        self.grid = Grid(self.screen, self.settings)
        self.tick_rate = self.settings.tick_rate

        # Simulation Indicatior
        self.sim_ind_font = pygame.font.Font(None, 30)
        self.sim_ind_surf = self.sim_ind_font.render('Simulating', True, 'Green')
        self.sim_ind_rect = self.sim_ind_surf.get_rect(topleft = (10, 10))


    def run_game(self):
        while self.running:
            self._check_events()

            if self.spawning:
                self.grid.spawn(pygame.mouse.get_pos())

            if self.killing:
                self.grid.kill(pygame.mouse.get_pos())

            self.screen.fill("black")

            if self.simulation:
                self.grid.update_grid()
                self.screen.blit(self.sim_ind_surf, self.sim_ind_rect)

            self.grid.draw_grid()

            pygame.display.flip()
            self.clock.tick(self.tick_rate)

        pygame.quit()
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.spawning = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.spawning = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.simulation = not self.simulation
                elif event.key == pygame.K_r:
                    self._reset_grid()

    def _reset_grid(self):
        self.grid.reset_grid()


if __name__=="__main__":
    game = GameOfLife()
    game.run_game()



