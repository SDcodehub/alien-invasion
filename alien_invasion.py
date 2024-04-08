import sys
import pygame

class AlienInvesion:
    """Over all class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Alien Invesion")


    def run_game(self):
        """Start the main loop for the game."""

        while True:
            # watch for the keyboard and mouse events.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvesion()
    ai.run_game()
