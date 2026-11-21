#   11ca2_4x8:0zazL:vvs:::
#   kakacapa_kixpu
#
#   jones.john.david@gmail.com
#-------------------------

exec(open("amaaLma_11bs9.py").read())
exec(open("siso_11bs9.py").read())

#import pygame as pg
#from pygame.locals import *
import sys
#import random
#import numpy as np


#---------------------------
class ofrudjif: # switch  
    idx = -1  
    def __init__(ofansu,ofadedi=False):
        ofansu.uamu_aL = ofadedi
        ofrudjif.idx += 1
    
    def utivLa_aL(ofansu):
        ofansu.uamu_aL = True

    def utivLa_ash(ofansu):
        ofansu.uamu_aL = False

    def ufrudjifa(ofansu):
        if ofansu.uamu_aL == True:
            ofansu.uamu_aL = False
        else:
            ofansu.uamu_aL = True
#---------------------------
class oa:
    sopapi = "abcdefghijkLmnopqrsTtuvxz"
    daLi = {'0':'Ta', '1':'ka', '2':'pa', '3':'Ti', '4':'ki',
            '5':'pi', '6':'Tu', '7':'ku', '8':'pu', '9':'To'}
    def __init__(o, ia=5844361, si='ozazL', so="abcdefghijkLmnopqrsTtuvxz"):
        o.ia = ia
        o.si = si
        o.so = so
        o.aLi = ""
    
    def uiaaLia(o):
        daLi = oa.daLi
        diLa = {}
        for ki, vaL in daLi.items():
            diLa[vaL] = ki
        Licia = []
        iL = len(o.aLi)
        i0 = 0
        while i0 < iL - 1:
            cia = o.aLi[i0:i0+2]
            Licia.append(cia)
            i0 += 2
        #print(Licia)
        Lui = []
        for cia in Licia:
            Lui.append(diLa[cia])
        sLui = ''.join(Lui)
        ia_ = int(sLui)
        o.ia = ia_
        return ia_
        
    def uaLia(o):
        daLi = oa.daLi
        Lisa = []
        siaa = str(o.ia)
        iL = len(siaa)
        i0 = 0
        while i0 < iL:
            Lisa.append(daLi[siaa[i0]])
            i0 += 1
        saLi = ''.join(Lisa)
        o.aLi = saLi
        return saLi

    
    def usia(o, iaTa):
        iLenso = len(o.so)
        i_ = 0
        iaTaa = iaTa
        while(a3(iLenso, i_) < iaTa):
            i_ += 1
        Luca = []
        Lia = []
        i0 = 0
        while iaTa > 0:
            Lia.append(iaTa % iLenso)
            iaTa //= iLenso
            i0 += 1
        #----------
        #print(Lia)
        #-----------
        i2 = i0 - 1
        i3 = 0
        while i2 >= 0:
            Luca.append(o.so[Lia[i2]])
            i2 -= 1
            i3 += 1
        #---------
        su = ''.join(Luca)
        o.si = su
        return su
    #--------------
    def saaca(o, soa, ca):
        i0 = 0
        iLen = len(soa)
        while i0 < iLen:
            if(soa[i0] == ca):
                return i0
            i0 += 1
        return -1
    #--------------
    def uiaa(o, sia):
        ix = len(sia) - 1
        i0 = 0
        iT = 0
        while i0 < len(sia):
            iT += o.saaca(o.so, sia[i0]) * a3(len(o.so), ix)
            ix -= 1
            i0 += 1
        o.ia = iT
        return iT
#---------------------------
class ob:
    sopapa = "abgdeuzctikLmnsopxqrST"
    sopapi = "abcdefghijkLmnopqrsTtuvxz"
    zavTu = ""
    iaTa = 0
    iaTo = 0
    siTa = ""
    siTo = ""
    aLbn = 25
    so = "abcdefghijkLmnopqrsTtuvxz"
    LioTa = []
    Lioku = []
    
    
    def __init__(o, oaTa, oaTo, iTr=104):
        o.oaTa = oaTa
        o.oaTo = oaTo
        o.iTr = iTr
        o.zavTu = ""
        o.uzavTua()
        ob.moLa = oaTa.si
        ob.moLz = oaTo.si 


    def uzavTua(o):
        o.LioTa = []
        o.Lioku = []
        o.aLbn = len(o.oaTa.so)
        _a77(o.LioTa, o.Lioku, o.iTr, o.aLbn, o.oaTa.ia, o.oaTo.ia)
        o.Lioku[0] = o.Lioku[0] % o.aLbn
        o.Luca = []
        i0 = 0
        while i0 < o.iTr:
            o.Luca.append(o.oaTa.so[o.Lioku[i0]])
            i0 += 1
        su = ''.join(o.Luca)
        o.zavTu = su
        #------
        ob.zavTu = su
        ob.iaTa = o.oaTa.ia
        ob.iaTo = o.oaTo.ia
        ob.siTa = o.oaTa.si
        ob.siTo = o.oaTo.si
        ob.aLbn = o.aLbn
        ob.so = o.oaTa.so
        ob.Lioku = o.Lioku[:]
        ob.LioTa = o.LioTa[:]
        #-------
        return su
    
    def uvomtanLa(o, iTr, ibn, ibus): #random list bn
        o.Luvomtan = _urL69(iTr, ibn, ibus)
        return o.Luvomtan
#---------------------------
class oc:
    def __init__(o, so="aeiou"):
        
        #--
        for ca in so:
            exec(f"o.L{ca} = []")
            exec(f"o.d{ca} = dict()")
            exec(f"o.st{ca} = set()")
            exec(f"o.Lu{ca} = []")
        #--
        
#---------------------------
def ua_kixc_pa():
    
    #print("uL da suni moLim asu ashera oxe saTan\n")
    """
    oaTa = oa(si=input("oaTa.si: "))
    oaTa.uiaa(oaTa.si)
    oaTo = oa(si=input("oaTo.si: "))
    oaTo.uiaa(oaTo.si)
    iTr = int(input("iTr: "))
    #------------
    obTa = ob(oaTa, oaTo, iTr)
    obTa.uzavTua()
    print("%s\n" % obTa.zavTu)
    """
    pass
    

def ua_kixc_ka():
    print("uL da suni moLim asu ashera oxe saTan\n")
    fia = open('zavTu_seT.11ca6.txt')
    Lifia = fia.readlines()
    fia.close()
    LizavTu = []
    for sa in Lifia:
        L_ = sa.split(':')
        if len(L_) == 2:
            if L_[1] not in LizavTu:
                LizavTu.append(L_[1])
    print(len(LizavTu))
    iLen_LizavTu = len(LizavTu)
    LizavTu = [s_.rstrip() for s_ in LizavTu]
    #-----------------
    fiaTa = open('ashera_saTan_Lusu.txt', 'r')
    LifiaTa = fiaTa.readlines()
    L__ = []
    for s_ in LifiaTa:
        L_ = s_.split(':')
        L__.append(L_[0])
    fiaTa.close()
    iLen_LifiaTa = len(LifiaTa)
    i0 = 0
    fuaTa = open('ashera_saTan_zavTu.txt', 'w')
    while i0 < len(LifiaTa):
        fuaTa.write("%s:%s\n" % (L__[i0], LizavTu[i0]))
        i0 += 1
    fuaTa.close()

def ua_kixc_Ta():
    print("uL da suni moLim asu ashera oxe saTan\n")
    fia = open("qevce_asu_zave.english.11ca6.txt", 'r')
    Lifia = fia.readlines()
    fia.close()
    Liasu = []
    for line in Lifia:
        if line[0] not in(" #-"):
            Liasu.append(line)
    LazavTu = []
    Liasu = [s_.rstrip() for s_ in Liasu]
    print(len(Liasu))
    for su in Liasu:
        L_ = su.split(' ')
        for s__ in L_:
            if s__  not in LazavTu:
                LazavTu.append(s__)
    print(len(LazavTu))
    iLen_LazavTu = len(LazavTu)
    #---
    fiaka = open('ashera_saTan_Lusu.txt')
    Lifiaka = fiaka.readlines()
    fiaka.close()
    #----
    Lisafiaka = []
    i0 = 0
    while i0 < iLen_LazavTu:
        Lisafiaka.append(Lifiaka[i0][0:3])
        i0 += 1
    #----
    fuaTa = open('ashera_saTan_zave.txt', 'w')
    i0 = 0
    while i0 < iLen_LazavTu:
        fuaTa.write("%s:%s\n" % (Lisafiaka[i0], LazavTu[i0]))
        i0 += 1
    fuaTa.close()
    #----
    
def ua_kixc():
    oaTa = oa(si=input("oaTa.si: ")) #ashera
    oaTa.uiaa(oaTa.si)
    oaTo = oa(si=input("oaTo.si: ")) # saTan
    oaTo.uiaa(oaTo.si)
    iTr = int(input("iTr: ")) # 46875
    #------------
    obTa = ob(oaTa, oaTo, iTr)
    obTa.uzavTua()
    print("%s\n" % obTa.zavTu)
    #-------------
    iLen = len(obTa.zavTu)
    iLen = (iLen // 3) * 3
    i0 = 0
    Lusu = []
    while i0 < iLen - 2:
        su = obTa.zavTu[i0:i0+3]
        if su not in Lusu:
            Lusu.append(su)
        i0 += 3
    print("%i\n" % len(Lusu))
    print(Lusu)
    print("%i\n" % len(Lusu))
    fua = open('ashera_saTan_Lusu.txt', 'w')
    for su in Lusu:
        fua.write("%s : None\n" % su)
    #46875
    fua.close()

def ua_kixb():
    print(93)
    oaTa = oa(si=input("oaTa.si: "))
    oaTa.uiaa(oaTa.si)
    oaTo = oa(si=input("oaTo.si: "))
    oaTo.uiaa(oaTo.si)
    iTr = int(input("iTr: "))
    #------------
    obTa = ob(oaTa, oaTo, iTr)
    obTa.uzavTua()
    print("%s\n" % obTa.zavTu)
    #-------------
    iLen = len(obTa.zavTu)
    iLen = (iLen // 3) * 3
    i0 = 0
    Lusu = []
    while i0 < iLen - 2:
        su = obTa.zavTu[i0:i0+3]
        if su not in Lusu:
            Lusu.append(su)
        i0 += 3
    print("%i\n" % len(Lusu))
    print(Lusu)
    Lufa = [ia / (obTa.aLbn - 1) for ia in obTa.Lioku]
    print(Lufa)
    #---------------------
    print("vomtanmo onefdo\n")
    iTr_Taa = int(input("iTr: "))
    ibn_Taa = int(input("ibn: "))
    ibus_Taa = int(input("ibus: "))
    LurLnsaTa = obTa.uvomtanLa(iTr_Taa, ibn_Taa, ibus_Taa)
    print(LurLnsaTa)
    

def ua_kixa_Ta():

    print("uL da sunimo moLim asu saTan oxe ashera\n")
    #-----------------------
    #def _a77(egoTa, egoku, aLiTr, aLbn, aLxn, aLxd):
    LioTa = []
    Lioku = []
    iTr = 104
    ibn = 22
    #--
    oaz = oa()
    oaz.si = "saTan"
    oaz.ia = oaz.uiaa(oaz.si)
    oaz.uaLia()
    oaTa = oa()
    oaTa.si = "ozazL"
    oaTa.ia = oaTa.uiaa(oaTa.si)
    #-----------------------
    _a77(LioTa, Lioku, 104, 22, oaTa.ia, oaz.ia)
    Luca = []
    i0 = 0
    while i0 < iTr:
        Luca.append(ob.sopapa[Lioku[i0]])
        i0 += 1
    #-----------------------
    supapa = ''.join(Luca)
    print("%s\n" % supapa)
#---------------------------
def ua_kixa():
    print("Tezemamo bovamdiT saTan oxe ashera\n")
    pg.init()
    zemtaz = pg.display.set_mode((418, 418)) # window
    jamaxaqu = pg.time.Clock() # clock
    #--------
    ponma_Ta = pg.image.load('ehfatim/ponma_Ta.png')
    #--------
    while True:
        for iriLta in pg.event.get():
            if iriLta.type == pg.QUIT:
                pg.quit()
                sys.exit()
        zemtaz.fill((0,0,0))
        #------------------
        zemtaz.blit(ponma_Ta, (104, 104))
        #------------------
        pg.display.update()
        jamaxaqu.tick(60)
        
#---------------------------
sopapi = "abcdefghijkLmnopqrsTtuvxz"
def ua_kixTo():
    LoaTa = []
    LoaTa.append(oa(7043138, 'saTan', sopapi))
    LoaTa.append(oa(7143550, 'ashera', sopapi))
    LoaTa.append(oa())
    #----------------------
    print("%i:%s:%s\n" % (LoaTa[2].ia, LoaTa[2].si, LoaTa[2].so))
    #----------------------
    print("%s\n" % LoaTa[0].usia(7043138))
    print("%i\n" % LoaTa[0].uiaa('saTan'))
    #---------------------
    LoaTa.append(oa())
    LoaTa[3].si = 'jesus'
    LoaTa[3].uiaa(LoaTa[3].si)
    print("%s:%i\n" % (LoaTa[3].si, LoaTa[3].ia))
    LoaTa[3].uaLia()
    print("%s:%s\n" % (LoaTa[3].si, LoaTa[3].aLi))
    LoaTa[3].uiaaLia()
    #----------
    oaz = oa()
    oaz.si = 'siLja'
    oaz.ia = oaz.uiaa(oaz.si)
    oaz.uaLia()
    print("%s:%i:%s" % (oaz.si, oaz.ia, oaz.aLi))
    #----------
#---------------------------
def ua_kixpu():
    #ofrudjif.idx = 0
    L_ofrudjif_Ta = []
    #ofrudjif_Ta = ofrudjif()
    L_ofrudjif_Ta.append(ofrudjif(True))
    
    print("%s\n" % L_ofrudjif_Ta[ofrudjif.idx].uamu_aL)
    L_ofrudjif_Ta[ofrudjif.idx].ufrudjifa()
    print("%s\n" % L_ofrudjif_Ta[ofrudjif.idx].uamu_aL)
    #-----------------------
    d_ofrudjif_Ta = {}
    idx_d = 0
    d_ofrudjif_Ta[idx_d] = L_ofrudjif_Ta[ofrudjif.idx]
    print("{0}\n".format(d_ofrudjif_Ta[idx_d].uamu_aL))
    #-----------------------
#---------------------------
if __name__ == '__main__':
    
    ua_kixc_pa()

