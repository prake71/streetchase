import pygame
import gamemode

class AttractMode(gamemode.GameMode):
    """ Attract Mode - get the player excited to play our game """
    def __init__(self, screen, game, message="Street Chase"):
        super().__init__(screen, game, message) # calls constructor of base class
#1
        self.name = "AttractMode"
        self.message = message


    def enter(self):
        self.active = True

    def update(self):
        #self.intro_sprite_list.update()
        pass

    def draw_frame(self):
        self.screen.fill([0,0,0])
        pygame.display.flip()

    def exit(self):
        self.active = False



