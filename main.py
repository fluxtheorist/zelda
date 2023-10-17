import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):
        # general setup
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.window_name = pygame.display.set_caption("Zelda")
        self.level = Level()

    def run(self):
        # running display
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
