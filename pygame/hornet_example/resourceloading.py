#!/usr/bin/env python3
"""Help functions to load images and sounds from disk into pygame
"""
import sys

import pygame
from pygame.locals import *

def load_images():
    """Loads images from disk and sets their color key (e.g. which color will be
    seen as transparent to pygame)
    
    Returns a image_name: image dictionary
    """
    image_name_and_paths = [
        ("hornet", "images/hornet.png"),
    ]
    PINK = (255,0,255)
    BLACK = (0, 0, 0)
    #TRANSPARENCY_COLOR is the color that will be seen as transparent to pygame
    TRANSPARENCY_COLOR = BLACK
    img = {}
    for name, path in image_name_and_paths:
        try:
            img[name] = pygame.image.load(path).convert()
            img[name].set_colorkey(TRANSPARENCY_COLOR)
        except:
            print(e)
            print("Couldn't load", path, "\nExiting")
            sys.exit()
    return img
    
def load_sounds():
    """Loads sounds from disk.
    Returns a sound_name: sound dictionary
    """
    sound_name_and_paths = [
    ]
    
    so = {}
    for name, path in sound_name_and_paths:
        try:
            so[name] = pygame.mixer.Sound(path)
        except:
            print("Couldn't load", path, "\nExiting")
            sys.exit()
    return so
