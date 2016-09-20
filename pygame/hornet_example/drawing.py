#!/usr/bin/env python3
import pygame
from pygame.locals import *

def draw_game(surface, img, fnt, game_dict):
    """Function that draws
    """
    #Start with a "blank slate" by writing a solid background color:
    surface.fill(game_dict["bg_color"])
    
    draw_hornet(surface, img, game_dict)
    
    #This is what actually draws the surface to the screen
    pygame.display.update()
    
def draw_hornet(surface, img, game_dict):
    #See http://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
    #surface.blit(source, dest)
    hornet_position = (game_dict["hornet_x"], game_dict["hornet_y"])
    surface.blit(img["hornet"], hornet_position)
