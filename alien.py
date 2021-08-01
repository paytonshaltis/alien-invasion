import pygame, pygame.display, pygame.image

class Alien(pygame.sprite.Sprite):
    """A class to represent a single Alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the Alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the Alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new Alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the Alien's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the Alien to the right."""
        self.x += self.settings.alien_speed
        self.rect.x = self.x