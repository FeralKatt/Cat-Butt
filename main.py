import ptext, pygame, sys
from pygame import *

""" 
This is just a VERY horrible demonstration on moving images and using Rects. And when I say horrible I means atrocious 
It is not a game it's just a Python program that moves a "CATBUTT" around 
with some added DEBUG displays.

I made this for myself but if it helps anyone else feel free to attribute so.

Loosely based off of Introduction to PyGame by sentdex
https://pythonprogramming.net/pygame-python-3-part-1-intro/

"""

DEBUG = True
FPS = 60
FPSCLOCK = pygame.time.Clock()

""" There are more colors here than used below just for example sake"""
CYAN      = (255,   0, 255)
DARK_GREY = ( 90,  90,  90)
BLACK     = (  0,   0,   0)
BLUE      = (  0,   0, 255)
GREEN     = (  0, 255,   0)
GREY      = (128, 128, 128)
NAVY      = (  0,   0, 125)
PURPLE    = (150,   0, 150)
PURPLE_D  = (100,   0, 100)
RED       = (255,   0,   0)
WHITE     = (255, 255, 255)

defaultFont = pygame.font.SysFont('comicsansms', 15)
defaultFontColor = WHITE

poop = "Look at by butthole"

WINDOW_X = 1280
WINDOW_Y = 720

CATTBUTTWIDTH = 50
CATTBUTTHEIGHT = 175

"""This is more complicated than sentex's  window because I'm doing a bit more and will work on adding resizing"""
GDX1 = int(WINDOW_X / 3)
GDX2 = GDX1 * 2

"""GDX1 is GAME DISPLAY divided by 3 and GDX 2 is GDX1 * 2, this is to get a frame 0.66"""


IDX1 = int(WINDOW_X / 3)
IDX2 = IDX1 * 2

DXY = WINDOW_Y - 5

GAMEDISPLAY = pygame.Rect(2, 2, GDX2, DXY)  # Left Display
INFODISPLAY = pygame.Rect(IDX2, 2, IDX1, DXY)  # Right Display

pygame.init()

"""CALLS FOR VARIABLES TO SET DISPLAY [] is list setting for x, y"""
SCREEN = pygame.display.set_mode((WINDOW_X, WINDOW_Y), 0, 0)
pygame.display.set_caption('Cat Butt')

running = True

catbuttImg = pygame.image.load('cat_butt.png')


def cat_butt(x, y):
    SCREEN.blit(catbuttImg, (x, y))



def main():
    CatbuttX = int(GDX2 * 0.45)
    CatbuttY = int(DXY * 0.8)
    x_change = 0
    y_change = 0

    mousex = 0
    mousey = 0

    while running:
        mouseClicked = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                if event.key == pygame.K_d:
                    x_change = 5
                if event.key == pygame.K_w:
                    y_change = -5
                if event.key == pygame.K_s:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        CatbuttX += x_change
        CatbuttY += y_change
        SCREEN.fill(DARK_GREY)

        """Shows current debug stats in display"""
        if DEBUG:  # DEBUG MENU
            ptext.draw('DEBUG', (50, 50),
                       fontname='deadman.ttf', fontsize=25,
                       color='red')
            DEBUG_Fps = str(FPSCLOCK)
            DEBUG_CatbuttX = str(CatbuttX)
            DEBUG_CatbuttY = str(CatbuttY)
            DEBUG_MouseX = str(mousex)
            DEBUG_MouseY = str(mousey)

            debugFont = pygame.font.SysFont('comicsansms', 15)
            debugFontColor = WHITE
            if mouseClicked:
                print(DEBUG_MouseY, DEBUG_MouseX)

            fpsSurfObj = debugFont.render(DEBUG_Fps, True, debugFontColor)
            fpsDB = fpsSurfObj

            CatbuttXSurfObj = debugFont.render(DEBUG_CatbuttX, True, debugFontColor)
            CatbuttX_DEBUG = CatbuttXSurfObj

            CatbuttYSurfObj = debugFont.render(DEBUG_CatbuttY, True, debugFontColor)
            CatbuttY_DEBUG = CatbuttYSurfObj

            mousexSurfObj = debugFont.render(DEBUG_MouseY, True, debugFontColor)
            mouseX_DEBUG = mousexSurfObj

            mouseySurfObj = debugFont.render(DEBUG_MouseX, True, debugFontColor)
            mouseY_DEBUG = mouseySurfObj

            SCREEN.blit(fpsDB, (100, 100))
            SCREEN.blit(CatbuttX_DEBUG, (100, 120))
            SCREEN.blit(CatbuttY_DEBUG, (100, 140))
            SCREEN.blit(mouseX_DEBUG, (100, 160))
            SCREEN.blit(mouseY_DEBUG, (100, 180))
            """END DEBUG"""

        pygame.draw.rect(SCREEN, BLACK, GAMEDISPLAY, 6)  # Last number sets border
        pygame.draw.rect(SCREEN, BLACK, INFODISPLAY, 6)

        cat_butt(CatbuttX, CatbuttY)

        if CatbuttX > (GDX2 - 45) - CATTBUTTWIDTH:
            CatbuttX = int(GDX2 - 90)
            poopFont = defaultFont
            poopSurfObj = poopFont.render(poop, True, WHITE)
            SCREEN.blit(poopSurfObj, INFODISPLAY.center)
        elif CatbuttX < 0:
            CatbuttX = 0
            poopFont = defaultFont
            poopSurfObj = poopFont.render(poop, True, WHITE)
            SCREEN.blit(poopSurfObj, INFODISPLAY.center)

        if CatbuttY > (DXY + 75) - CATTBUTTHEIGHT:
            CatbuttY = int(DXY - 100)
            poopFont = defaultFont
            poopSurfObj = poopFont.render(poop, True, WHITE)
            SCREEN.blit(poopSurfObj, INFODISPLAY.center)
        elif CatbuttY < 0:
            CatbuttY = 0
            poopFont = defaultFont
            poopSurfObj = poopFont.render(poop, True, WHITE)
            SCREEN.blit(poopSurfObj, INFODISPLAY.center)

        pygame.display.flip()
        FPSCLOCK.tick(FPS)


main()
pygame.quit()
quit()


