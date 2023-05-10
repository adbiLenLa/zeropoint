#11bam/3xs:0z:vV:::
#
#    john.david jones
#    ozazL
#    vanhan vaasan sairaaLa
#------------
import pygame as pg 
from pygame.locals import *
from random import randint
import math

exec(open('azq_zdd_11ba9.py').read())

fps = pg.time.Clock()
FPS = 60

pg.init()
sc_w = 418
sc_h = 418
_ds = pg.display.set_mode((sc_w, sc_h), 0, 32)
pg.display.set_caption('pg_sina_11bam')
b_x = 0
b_xh = sc_w // 2
b_yh = sc_h // 2
d_aL = 0.0
d_inc = 0.1
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
    b_x = -b_xh
    _ds.fill((0,0,0))
    d_aL += d_inc 
    while b_x < b_xh:
        d_aL += (math.pi * 2) / sc_w
        
        b_y = math.sin(d_aL) * 108
        #r_cLr = (urI(256), urI(256), urI(256))
        L__ = _urL(26, 256)
        r_cLr = (L__[21], L__[22], L__[23])
        #r_pos = (randint(0, 417), randint(0, 417))
        b_xp = b_x + b_xh
        b_yp = b_yh - b_y
        r_pos = (int(b_xp), int(b_yp))
    
        _ds.set_at(r_pos, r_cLr)
    #b_x += (2 * math.pi) / 3600
        b_x += 1
    fps.tick(FPS)
    pg.display.update()



