
"""
Edited By: Colm Keyes


"""

"""
    Ahira Justice, ADEFOKUN
    justiceahira@gmail.com
"""

import os
import sys
import pygame
from pygame.locals import *
from chessboard import Application
from time import sleep

from . import board
import tkinter as tk
import subprocess

#os.environ['SDL_VIDEO_CENTERED'] = '1' # Centre display window.

FPS = 30
FPSCLOCK = pygame.time.Clock()

DISPLAYSURF = None

BASICFONT = None

gameboard = None

colors = {
    'Ash':  ( 50,  50,  50),
    'White':(255, 255, 255),
    'Black':(  0,   0,   0),
}

BGCOLOR = colors['Ash']

WINDOWWIDTH, WINDOWHEIGHT = 600, 600

BASICFONTSIZE = 30


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() #terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back
    
    return False


def start( fen='' ):

    global gameboard


    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('LOCI')
    #BASICFONT = pygame.font.SysFont('calibri', BASICFONTSIZE)

    checkForQuit()

    DISPLAYSURF.fill(BGCOLOR)
    gameboard = board.Board(colors, BGCOLOR, DISPLAYSURF)
    gameboard.displayBoard([],[])

    #root.update_idletasks()
    pygame.display.init()
    pygame.display.update()
    FPSCLOCK.tick(FPS)

def update(fen, attack_squares_coords, attack_squares_coords_behind):
    checkForQuit()
    gameboard.displayBoard(attack_squares_coords, attack_squares_coords_behind)
    #gameboard.updatePieces(fen)

    pygame.display.update()
    #root.update()
    FPSCLOCK.tick(FPS)

