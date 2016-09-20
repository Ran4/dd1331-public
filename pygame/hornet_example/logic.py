#!/usr/bin/env python3
import math

import pygame
from pygame.locals import *
    
def get_hornet_displacement(game_dict, key):
    """Returns how much we should change the x/y values when moving the
    hornet. If we're moving diagonally, we shouldn't move at full speed,
    since we'll be moving in two directions at once
    """
    speed = game_dict["hornet_speed"]
    
    is_holding_diagonal = (key[K_LEFT] or key[K_RIGHT]) \
        and (key[K_UP] or key[K_DOWN])
        
    if is_holding_diagonal:
        return speed / 2**0.5
    else:
        return speed
    
def handle_hornet_movement(game_dict, key):
    displacement = get_hornet_displacement(game_dict, key)
    
    if key[K_LEFT]:
        game_dict["hornet_x"] -= displacement
    elif key[K_RIGHT]:
        game_dict["hornet_x"] += displacement
    if key[K_UP]:
        game_dict["hornet_y"] -= displacement
    elif key[K_DOWN]:
        game_dict["hornet_y"] += displacement
        
def apply_wind_to_hornet(game_dict):
    wind_x = -0.8
    seconds_since_start = game_dict["game_time"] / float(game_dict["framerate"])
    wind_y = 1.5 * math.sin(2 * seconds_since_start)
    game_dict["hornet_x"] += wind_x
    game_dict["hornet_y"] += wind_y

def handle_logic(img, so, game_dict):
    mpos = pygame.mouse.get_pos()
    mbut = pygame.mouse.get_pressed()
    key = pygame.key.get_pressed()
    
    #Here goes game logic
    handle_hornet_movement(game_dict, key)
    #Uncomment below line to "add wind" to hornet
    #apply_wind_to_hornet(game_dict)
    
    game_dict["game_time"] += 1
