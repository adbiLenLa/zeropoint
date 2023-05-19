#11bav/3y1:0z:vV:::
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
#--
b__i = 11
pg.font.init()
my_font = pg.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render(f"{b__i}", False, (255, 255, 255))


#--
fps = pg.time.Clock()
FPS = 60

pg.init()
sc_w = 418
sc_h = 418
_ds = pg.display.set_mode((sc_w, sc_h), 0, 32)
pg.display.set_caption('pg_eLikam_11bav')
b_x = 0
b_xh = sc_w // 2
b_yh = sc_h // 2
d_aL = 0.0
d_inc = 1.0 / 18
d_xd = 0.0
b__n = 5
my_pi = round(22 / 7.0, 6)
#b__i = 11
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                b__i += 1 #number of rings
            if event.key == pg.K_DOWN:
                b__i -= 1
                if b__i < 0:
                    b__i = 0
            if event.key == pg.K_RIGHT:
                b__n += 1
                
            if event.key == pg.K_LEFT:
                b__n -= 1
            if event.key == pg.K_f:
                FPS += 1
            if event.key == pg.K_s:
                FPS -= 1
                if FPS <= 0:
                    FPS = 1
                
    b_x = -b_xh
    _ds.fill((0,0,0))
    #d_aL +=  (math.pi * 2.0) / (math.pi**b__n)
    while b_x < b_xh:
        d_aL += (my_pi * 2.0) / (my_pi**b__n)
        if d_aL >= (my_pi * 2.0):
            d_aL = 0.0
        
        b_y = math.sin(d_aL) * 108 * (d_xd - 0.0)
        b__x = math.cos(d_aL) * 108 * d_xd
        d_xd += a7d(1.0 , b__i)
        if d_xd > 1.0:
            d_xd = 0.0
        #L__ = _urL(26, 256)
        #r_cLr = (L__[6], L__[11], L__[23])
        r_cLr = (255, 255, 255)
        b_xp = b__x + b_xh
        b_yp = b_yh - b_y
        r_pos = (int(b_xp), int(b_yp))
    
        _ds.set_at(r_pos, r_cLr)
        b_x += (2 * my_pi) / (my_pi**3)
        #--
        
        text_surface = my_font.render(f"{b__i}:{b__n}:{FPS}", False, (255, 255, 255))
        _ds.blit(text_surface, (0,0))
    fps.tick(FPS)
    pg.display.update()



