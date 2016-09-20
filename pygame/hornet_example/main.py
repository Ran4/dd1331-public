#!/usr/bin/env python3
import sys

import pygame
from pygame.locals import *

import logic
import drawing
import resourceloading

def set_screen(game_dict, toggle_fullscreen=False):
    if toggle_fullscreen:
        game_dict["fullscreen"] = not game_dict["fullscreen"]
    
    if game_dict["fullscreen"]:
        return pygame.display.set_mode(game_dict["screensize"], FULLSCREEN)
    else:
        return pygame.display.set_mode(game_dict["screensize"])
    
def get_initial_game_dict():
    LIGHT_BLUE = (135,206,250) # Color tuple (R, G, B) == (Red, Green, Blue)
    SCREENSIZE = (800, 600)
    game_dict = {
        "exit": False, # Set to True to exit next frame
        "framerate": 60, # Number of frames per second
        "game_time": 0, # Number of total elapsed frames
        "bg_color": LIGHT_BLUE,
        "screensize": SCREENSIZE, # Size of window in pixels
        "screenw": SCREENSIZE[0], # Height of window in pixels
        "screenh": SCREENSIZE[1], # Width of window in pixels
        "fullscreen": False,
        "hornet_x": 400,
        "hornet_y": 300,
        "hornet_speed": 4,
        }
    return game_dict

def setup():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Python+Pygame game")
    
    game_dict = get_initial_game_dict()
    screen = set_screen(game_dict)
    pygame.mixer.init()
    
    try:
        fonts = pygame.font.Font(None, 22) #font of size (=height) 22
        print("Loaded default font")
    except: #couldn't load default font, tries to load manually
        print("Couldn't load default font")
        fonts = pygame.font.SysFont("arial", 16)
        print("Loaded arial font")
    
    #load images, sounds and classes here
    image_dict = resourceloading.load_images()
    sound_dict = resourceloading.load_sounds()
    
    return clock, game_dict, screen, image_dict, sound_dict, fonts
    
def main():
    clock, game_dict, screen, img, so, fnt = setup()
    while not game_dict["exit"]:
        # Pygame has an event handler. Things like keyboard presses,
        # mouse clicks, screen resizes and other will be handled here:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_dict["exit"] = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_dict["exit"] = True
                elif event.key == K_RETURN: #ENTER toggles fullscreen
                    set_screen(game_dict, toggle_fullscreen=True)
                elif event.key == K_F1:
                    print("fps: %s" % round(game_dict["fps"], 1))
        
        # Perform the logic step, then the drawing step:
        logic.handle_logic(img, so, game_dict)
        drawing.draw_game(screen, img, fnt, game_dict)
        clock.tick(game_dict["framerate"]) # This is blocking
        game_dict["fps"] = clock.get_fps()
        
    # We've left the main loop, so let's quit. Call pygame.quit() to close our
    # window gracefully
    pygame.quit()
    sys.exit()
    
if __name__ == "__main__":
    main()
