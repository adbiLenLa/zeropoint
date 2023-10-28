#11bfd/42j:0zazL:vvs:::
#
#    john.david jones
#    ozazL
#    vanhan vaasan sairaaLa
#------------
"""
szfy the first spirit

jones.john.david@gmail.com

"""
import pygame as pg 
from pygame.locals import *
from random import randint 
import math
from sys import exit

exec(open('amaaLma_11bav.py').read())
exec(open('eLikaTakim_11bfd.py').read())

#------------------
"""
def _urL104(aLiTr, aLbn, adx=0):
    #return random list
    dT = datetime.today()
    dTus = dT.microsecond
    LegoTa, Legoku = _a77T(aLiTr, aLbn, dTus, 1000000 + adx)
    return(Legoku)

def _urL_ns104(aLiTr, aLbn, adx=0):
    dT_ns = tm.time_ns()
    LegoTa, Legoku = _a77T(aLiTr, aLbn, dT_ns, 1000000000 + adx)
    return(Legoku)
"""
#-------------------

#--------------------------
SCREEN_SIZE = (418, 418)
pg.init()
screen = pg.display.set_mode(SCREEN_SIZE, 0, 32)
pg.display.set_caption("pg_szfy_11bfd")

font = pg.font.SysFont("arial", 16)
font_height = font.get_linesize()
Lusa = ["szfy"]

screen.fill((0,0,0))

fps = pg.time.Clock()
FPS = 60
_adx = 0
while True:

    #event = pg.event.wait()
    
    for event in pg.event.get():
        if event.type == QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_f:
                    FPS += 1
            if event.key == pg.K_s:
                FPS -= 1
                if FPS <= 0:
                    FPS = 1
            if event.key == pg.K_UP:
                _adx += 1
            if event.key == pg.K_DOWN:
                _adx -= 1

    
    screen.fill((0, 0, 0))
    
    screen.blit( font.render(f"{Lusa[0]}:{FPS}:{_adx}", True, (255,255,255)), (213, 213) )
    
    #----
    #_adx = 0
    L__ = _urL_ns104(210, 418, _adx)
    #for _i in range(104):
    _i = 0
    while _i < 208:
        Trc = (255, 255, 255)
        
        
        Trp = (L__[_i], L__[_i + 1])
        _i += 2
        screen.set_at(Trp, Trc)
    
    
    #----
     
            
            
    #---------
    fps.tick(FPS)
    
    pg.display.update()
    
    