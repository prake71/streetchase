import pygame
import random
import gamemode
#import soundmanager
#from constants import *

class PlayMode(gamemode.GameMode):
    """ Play Mode """

    def __init__(self, screen, game, message="Play Mode", fps=60):
        super().__init__(screen, game, message, fps)
#1
        self.name = "PlayMode"
        self.game_over = False
        self.mode_exit_delay = 5 * fps # seconds * fps=60

        # Sprites and Spritelists
        self.player = None
        self.all_sprites_list = None
        # self.sm = soundmanager.SoundManager()

    def enter(self):
        """ enter mode """
        self.active = True # Playmode active

        # populate world with objects
        # Sprites and Spritelists

        # create 1st enemy wave


    def exit(self):
        self.active = False
        self.game_over = False
#        self.sm.stop_ambient()
        self.mode_exit_delay = 5 * self.fps

        #time.sleep(5)
    def _generate_enemy_wave(self, level=1):
        pass


    def update(self):
        pass


    def draw_frame(self):
        self.screen.fill([0, 0, 0])

        pygame.display.update()

    def handle_events(self):
        """ processing event Loop """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

