#11bfi/42o:0zazL:vvs:::
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
import tkinter as tk
from tkinter import ttk
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
class o:
    so = "0123456789abcdefghijklmnopqrstuvwxyz"
    li = []
    mol = ""
    ial = 0
    da = {}
    def __init__(az, mol, ial):
        az.mol = mol
        az.ial = ial
    def ugial(az, si):
        iu = 0
        for c_ in si:
            if c_ in az.so:
                iu += az.so.index(c_)
        return iu
#--------------------------

#--------------------------
import re
fiat = open("ozazL_11b9g.txt")
life = []
for line in fiat:
    life.append(line.strip())
fiat.close()
slife = set(life)
def uslife(sin):
    lu = []
    for o in slife:
        if sin in o:
            lu.append(o)
    return lu

def uxlife(prax):
    sux = rf'{prax}\b'
    rex = re.compile(sux)
    lusux = []
    for o in slife:
        if rex.match(o):
            lusux.append(o)
    return lusux

#--------------------------
SCREEN_SIZE = (418, 418)
pg.init()


#----------------------------------------------
"""

"""
#--------------------------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn0 = tk.Button(self, text="ok", command=self.say_hello)
        self.btn0.pack()
        #---
        self.btn1= tk.Button(self, text="load", command=self.load_file)
        self.btn1.pack()
        #---
        self.btn2 = tk.Button(self, text="clear", command=self.clear)
        self.btn2.pack()
        #---
        self.btn3 = tk.Button(self, text="save", command=self.save)
        self.btn3.pack()
        #---
        self.text0 = tk.Text(self, width=72, height=23)
        self.text0.pack()
        #---
        self.entry0text = tk.StringVar()
        self.entry0 = tk.Entry(self, textvar=self.entry0text)
        self.entry0.pack()
        #----
        self.label0 = tk.Label(self, text="siso is listening")
        self.label0.pack()
        self.label1 = tk.Label(self, text="uL da suni moL")
        self.label1.pack()
        #----
        
    def say_hello(self):
        self.sin = self.text0.get("1.0", tk.END)
        exec(self.sin)
        #print("boL ieue aLe suTnam")
        self.file_name = self.entry0.get()
        if self.file_name:
            fo = open(self.file_name, "w")
            fo.write(self.sin)
            fo.close()
    def load_file(self):
        file_name = self.entry0.get()
        fi = open(file_name, "r")
        s_ = fi.read()
        fi.close()
        self.text0.delete("1.0", tk.END)
        self.text0.insert("1.0", s_)
    def clear(self):
        self.text0.delete("1.0", tk.END)
    def save(self):
        file_name = self.entry0.get()
        su = self.text0.get("1.0", tk.END)
        fo = open(file_name, "w")
        fo.write(su)
        fo.close()
#------------------------
class CanvasApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("cap0")
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack()
            
#------------------------
app = App()
cap0 = CanvasApp()
app.title("szfy7i")
#-----------------------------------------------
screen = pg.display.set_mode(SCREEN_SIZE, 0, 32)
pg.display.set_caption("pg_szfy7i_11bfi")

font = pg.font.SysFont("arial", 16)
font_height = font.get_linesize()
Lusa = ["szfy"]

screen.fill((0,0,0))

fps = pg.time.Clock()
FPS = 60
_adx = 0
_anu = 3
#-----------
#sprite_image_filename = "_iszfy.png"
#sprite = pg.image.load(sprite_image_filename)
_ix = 0
i_y = font_height
s_Text = ""
#-----------
szfy = o("szfy", 112)
szfy.ial = szfy.ugial('szfy')
#-----------
while True:

    #-----------------------tkinter 
    #app.btn0.configure(text=s_Text)
    
    
    #-----------------------

    #event = pg.event.wait()
    
    for event in pg.event.get():
        if event.type == QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            s_Text += event.unicode
            if event.key == pg.K_BACKSPACE:
                s_Text = ""
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

    
    #screen.fill((0, 0, 0))
    #------------
    
    iaLaL  = szfy.ugial(s_Text)
    """
    if s_Text:
        lucy = uxlife(s_Text)
        if lucy:
            screen.blit( font.render(f"{lucy[0:2]}", True, (0,255,0)), (13, 93) )
            app.label0.configure(text=lucy[0:2])
    
    """
    #------------
    
    #screen.blit( font.render(f"{Lusa[0]}:{FPS}:{_adx}", True, (255,255,255)), (13, 36) )
    #screen.blit( font.render(f"{s_Text}", True, (0,255,0)), (13, 13) )
    #screen.blit( font.render(f"{iaLaL}", True, (0,255,0)), (13, 54) )
    #----
    #_adx = 0
    L__ = _urL_ns104(210, 418, _adx)
    #for _i in range(104):
    _i = 13
    
    L__L = []
    while _i < 208:
        Trc = (255, 255, 255)
        
        
        Trp = (L__[_i], L__[_i + 1])
        #L__L.append([L__[_i], L__[_i+1]])
        _i += 2
        #screen.set_at(Trp, Trc)
        
    __i = 13
    __i0 = 13
    
    while __i < __i0 + 3:
        L__L.append([L__[__i], L__[__i+1]])
        __i += 1
    
    #pg.draw.polygon(screen, (255,255,255), L__L)
    #pg.draw.lines(screen, (255, 255, 255), True, L__L, 1)
    #screen.blit(sprite, (_ix, 104))
    #pg.draw.circle(screen, (0,0,255), (_ix, 104), 13, 3)
    _ix += 3
    if _ix > 418:
        _ix = -26
    #----
    #button0.configure(text=s_Text)
    app.btn0.configure(text="doit")
    #app.label0.configure(text=lucy[0])
    #------   
    fi = open("szfy7i.py")
    las = fi.read()
    exec(las)
    fi.close()
        
    #---------
    fps.tick(FPS)
    
    pg.display.update()
    app.update()
    cap0.update()
    #root.update()