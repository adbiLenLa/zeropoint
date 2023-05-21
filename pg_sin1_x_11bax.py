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

exec(open('amaaLma_11bav.py').read())

fps = pg.time.Clock()
FPS = 60

pg.init()
sc_w = 418
sc_h = 418
_ds = pg.display.set_mode((sc_w, sc_h), 0, 32)
pg.display.set_caption('pg_sin1_x_11bax')
b_x = 0
b_xh = sc_w // 2
b_yh = sc_h // 2
d_aLa = -4.0 * math.pi
d_inc = 0.0
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
    b_x = -1 * b_xh
    #b_x = 1
    #b_x = 1.0
    _ds.fill((0,0,0))
    d_aL =  d_aLa
    while b_x < b_xh:
        #d_aL += (math.pi * 2) / (sc_w / 4.0)
        d_aL += ((math.pi * 2.0)/ 108)
        #if d_aL > math.pi * 4.0:
        #    d_aL = -4.0 * math.pi
        
        #b_y = a7d(math.sin(d_aL), d_aL) * 108
        #b_y = a7d(((b_x ** 2) - 1.0),(b_x - 1.0)) - 0
        #b_y = a7d((b_x + 2.0), b_x)
        #b_y = a7d((b_x**2 + b_x - 2.0), (b_x**2 - b_x))
        #b_y = d_aL**2 * math.sin(a7d(1.0, d_aL)) * 108.0
        b_y = math.sin(a7d(1.0,b_x/1080.0)) * 108.0 
        
        #b_y = (math.sin(d_aL) + math.cos(d_aL / 2.0))* 23
        L__ = _urL(26, 256)
        r_cLr = (L__[6], L__[11], L__[23])
        #r_cLr = (randint(0, 255), randint(0, 255), randint(0, 255))
        #r_pos = (randint(0, 417), randint(0, 417))
        b_xp = (b_x + b_xh) * 1.0
        b_yp = b_yh - b_y
        #b_yp = b_y
        #b_yp = b_xp ** 2
        r_pos = (int(b_xp), int(b_yp))
    
        _ds.set_at(r_pos, r_cLr)
        #b_x += (2 * math.pi) / 3600
        b_x += (math.pi * 2.0)/(math.pi**5)
        #b_x += 1.0
    fps.tick(FPS)
    pg.display.update()



