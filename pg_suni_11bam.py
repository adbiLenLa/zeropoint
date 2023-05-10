#11bam/3xs:0z:vV:::

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
pg.display.set_caption('so uamu unefdiLuLka')
b_x = 0
b_xh = sc_w // 2
b_yh = sc_h // 2
d_aLa = -4.0 * math.pi
d_inc = 0.0
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
    b_x = -b_xh
    _ds.fill((0,0,0))
    d_aL =  d_aLa
    while b_x < b_xh:
        d_aL += (math.pi * 2) / (sc_w / 4.0)
        
        b_y = a7d(math.sin(d_aL), d_aL) * 108
        r_cLr = (randint(0, 255), randint(0, 255), randint(0, 255))
        #r_pos = (randint(0, 417), randint(0, 417))
        b_xp = b_x + b_xh
        b_yp = b_yh - b_y
        r_pos = (int(b_xp), int(b_yp))
    
        _ds.set_at(r_pos, r_cLr)
    #b_x += (2 * math.pi) / 3600
        b_x += 1
    fps.tick(FPS)
    pg.display.update()



