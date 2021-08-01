import pygame, pygame.image, pygame.rect, pygame.sprite, pygame.draw

class Bullet(pygame.sprite.Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a Bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(
            0, 
            0, 
            self.settings.bullet_width, 
            self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the Bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the Bullet up the screen."""
        # update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        
        # update the rect position
        self.rect.y = self.y 

    def draw_bullet(self):
        """Draws the Bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)