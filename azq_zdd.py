# 11azo/3mu:ozazL:vanhavaasa:::
import math
import nltk
import re
from datetime import *

ssL = "boLieueaLestn"
soL = "abgdeuzctikLmnsopxqrST"
sos = "0123456789abcdefghijklmnopqrstuvwxyz"
#------------------------------------
def a0(bi, bn):
    if bn == 0:
        return(bi)
    else:
        return(bi % bn)

def a1(bia, bie):
    return(bia + bie)

def a2(bia, bie):
    return(bia * bie)

def a3(b, n):
    if b == 0 and n == 0:
        return(1)
    elif b == 0:
        return(0)
    else:
        return(b**n)

def a5(bb):
    return(abs(bb))

def a7(bn, bd):
    bL = 1
    if bd < 0:
        bd = -1 * bd
        bL = bL * -1
    if bn < 0:
        bn = -1 * bn
        bL = bL * -1
    if bn == 0 and bd == 0:
        return(1)
    elif bd == 0:
        return(0)
    else:
        bu = math.floor(bn / bd)
        return(bL * bu)
    
def a7d(da, de):
    if de == 0 and da == 0:
        return 1.0
    if de == 0:
        return 0.0
    else:
        return da / de
    

def _a77(egoTa, egoku, aLiTr, aLbn, aLxn, aLxd):
    #egoTa = []
    #egoku = []
    Lia = 0
    Lie = 0
    aLi = 0
    while Lia < aLiTr:
        aLi = 0
        while aLxn < aLxd:
            aLxn = aLxn * aLbn
            aLi = aLi + 1
            if aLi > 1:
                egoku.append(0)
                Lia = Lia + 1
                if Lia == aLiTr:
                    return(Lie)
        buS = a7(aLxn, aLxd)
        buS = a0(buS, aLbn)
        egoku.append(buS)
        #print(f"{buS}")
        aLxn = a0(aLxn, aLxd)
        egoTa.append(aLxn)
        Lia = Lia + 1
        Lie = Lie + 1
    return(Lie)


def a8(bia, bie):
    return(bia - bie)
#----------------------------------------------------
# fuLL capture
#----------------------------------------------------

#-----------------------------------------------------
def _u77T(Legokus, soo):
    bi = 0
    bz = len(Legokus)
    us = ""
    bLsoo = len(soo)
    while(bi < bz):
        ga = soo[a0(Legokus[bi], bLsoo)]
        us += ga
        bi = bi + 1
    return(us)

#assumes you have imported the nltk.book 
Lmwbb = []
#for sii in text3:
#    Lmwbb.append(sii)

#bbL = nltk.corpus.gutenberg.words('bible-kjv.txt')

#bbLc = []
#for os in bbL:
#    su = os.lower()
#    bbLc.append(su)

#SbbLc = set(bbLc)

#LbbLc = []

#for os in SbbLc:
#    LbbLc.append(os)
def _utfc(aLiTr, aLbn, so):
    dT = datetime.today()
    dTus = dT.microsecond
    LegoTa, Legoku = _a77T(aLiTr, aLbn, dTus, 1000000)
    usa = _u77T(Legoku, so)
    return(usa)

def _a77T(aLiTr, aLbn, aLxn, aLxd):
    egoTa = []
    egoku = []
    Lia = 0
    Lie = 0
    aLi = 0
    while Lia < aLiTr:
        aLi = 0
        while aLxn < aLxd:
            aLxn = aLxn * aLbn
            aLi = aLi + 1
            if aLi > 1:
                egoku.append(0)
                Lia = Lia + 1
                if Lia == aLiTr:
                    return(egoTa, egoku)
        buS = a7(aLxn, aLxd)
        buS = a0(buS, aLbn)
        egoku.append(buS)
        #print(f"{buS}")
        aLxn = a0(aLxn, aLxd)
        egoTa.append(aLxn)
        Lia = Lia + 1
        Lie = Lie + 1
    return(egoTa, egoku)


def uLLz():
    #genesis
    global LLz
    global sus21
    LLz = []
    sus21 = _utfc(718, 21, so21)
    uLsus21(sus21)
    #--
    for sii in LmwbbLc_:
        for si in Lsus21:
            if sV(sii) == si:
                LLz.append(f'{si}:{sii}')
                print(f'{si}:{sii}')

def uLLza():
    #bible-kjv
    global LLza
    global sus21
    LLza = []
    sus21 = _utfc(718, 21, so21)
    uLsus21(sus21)
    #--
    for sii in LbbLc:
        for si in Lsus21:
            if sV(sii) == si:
                LLza.append(f'{si}:{sii}')
                #print(f'{si}:{sii}')

so24 = soL + '_.'
s240 = _utfc(718, 24, so24)
Ls240 = re.split('[_.]', s240)

LL240 = []
def uLL240():
    #hebrewith finals
    global LL240
    s240 = _utfc(718, 24, so24)
    Ls240 = re.split('[_.]', s240)
    LL240 = []
    bi = 0
    bz = len(Ls240)
    while bi < bz:
        if len(Ls240[bi]) >= 1:
            ga = Ls240[bi][-1]
            su = Ls240[bi]
            if ga in "kmnpx":
                su = Ls240[bi][0:-1] + Ls240[bi][-1].upper()
                print(f'{su}')
                LL240.append(f'{su}')
        bi = bi + 1

LL240ba = []
def uLL240ba(ba):
    #hebrewith finals
    global LL240ba
    s240 = _utfc(ba, 24, so24)
    Ls240 = re.split('[_.]', s240)
    LL240 = []
    bi = 0
    bz = len(Ls240)
    while bi < bz:
        if len(Ls240[bi]) >= 1:
            ga = Ls240[bi][-1]
            su = Ls240[bi]
            if ga in "kmnpx":
                su = Ls240[bi][0:-1] + Ls240[bi][-1].upper()
                print(f'{su}')
                LL240ba.append(f'{su}')
        bi = bi + 1

def uLoox(boz, bn):
    Loox = _urL(boz, bn)
    Lu = []
    bi = 0
    while bi < boz:
        su = bbLc[Loox[bi]];
        print(f'{su}', end=" ")
        Lu.append(su)
        bi = bi + 1
    return(Lu)

def urI(bea):
    #returns random int
    LurI = _urL(108, bea)
    return(LurI[23])

#------------------------------------

def _urL(aLiTr, aLbn):
    #return random list
    dT = datetime.today()
    dTus = dT.microsecond
    LegoTa, Legoku = _a77T(aLiTr, aLbn, dTus, 1000000)
    return(Legoku)
    #usa = _u77T(Legoku, so)
    #return(usa)

def _urL93(aLiTr, aLbn):
    dT = datetime.today()
    dTus = dT.microsecond
    dT1 = datetime.today()
    dT1us = dT1.microsecond
    LegoTa, Legoku = _a77T(aLiTr, aLbn, dTus, dT1us)
    Legoku[0] = a0(Legoku[0], aLbn)
    return(Legoku)

Lsus21 = []
def uLsus21(sus21_):
    global Lsus21
    bi = 0
    bz = len(sus21_)
    while bi < bz - 3:
        su = sus21_[bi:bi + 3]
        Lsus21.append(su)
        bi += 1

def sV(sii):
    su = ''
    for bi in range(len(sii)):
        if sii[bi] not in "aeiou":
            su += sii[bi]
    return(su)


#--------------------------------------
