import sys
import pygame
from settings import Settings

class AlienInvesion:
    """Over all class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        pygame.display.set_caption("Alien Invesion")

        self.clock = pygame.time.Clock()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))


    def run_game(self):
        """Start the main loop for the game."""

        while True:
            # watch for the keyboard and mouse events.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    ai = AlienInvesion()
    ai.run_game()
