# importing external packages / modules
import sys
import pygame, pygame.display, pygame.event, pygame.sprite
from pygame.locals import *

# importing my own modules from this project
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class that will manage game behavior."""

    def __init__(self, screen):
        """Initialize the game and create needed resources."""
        pygame.init()
        
        # create a settings attribute for this game instance
        self.settings = Settings(screen)

        # set the screen dimensions and caption (this is a surface)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.scren_height))
        pygame.display.set_caption('Alien Invasion')

        # create a ship attribute for this game instance
        self.ship = Ship(self)

        # create a Group of live Bullet objects (from Sprite)
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        """Starts the main game loop."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()


    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():

            # closing the window quits the game
            if event.type == QUIT:
                sys.exit()

            # check certain event pased on event.type
            elif event.type == KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == K_RIGHT:
            self.ship.moving_right = True
        elif event.key == K_LEFT:
            self.ship.moving_left = True
        elif event.key == K_SPACE:
            self._fire_bullet()
        elif event.key == K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        if event.key == K_RIGHT:
            self.ship.moving_right = False
        elif event.key == K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new Bullet and add it to the 'bullets' list."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    game = AlienInvasion('AOC')
    game.run_game()