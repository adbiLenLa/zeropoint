#
#   11cad_4xj:0zazL:vvs:::
#   kakacad_kixj
#
#   jones.john.david@gmail.com
#--------------------------
exec(open("koLa_kixpu.py").read())
import json
#--------------------------
def ua_kixj_ka():
    print("onoTaashera etmesaTan")
    oaTa = oa(si=input("oaTa.si: "))
    #---
    if oaTa.si == "":
        oaTa.si = "ozazL"
    if oaTa.si[0] in "0123456789":
        oaTa.ia = int(oaTa.si)
        oaTa.si = oaTa.usia(oaTa.ia)
    #---
    oaTa.uiaa(oaTa.si)
    oaTo = oa(si=input("oaTo.si: "))
    if oaTo.si == "":
        oaTo.si = "adniboL"
    #---
    if oaTo.si[0] in "0123456789":
        oaTo.ia = int(oaTo.si)
        oaTo.si = oaTo.usia(oaTo.ia)
    #---
    if oaTo.si == "":
        oaTo.si = "adniboL"
    oaTo.uiaa(oaTo.si)
    iTr = int(input("iTr: "))
    if iTr < 3:
        iTr = 3
    obTa = ob(oaTa, oaTo, iTr)
    #----
    fia = open("adaLao_sunisamgu.txt", "r")
    Lisa = fia.readlines()
    fia.close()
    #----
    Lisa = [s_.rstrip() for s_ in Lisa]
    Luza = []
    daaT = {}
    for sa in Lisa:
        L_ = sa.split(':')
        daaT[L_[0]] = L_[1]
    #---
    obTa.uzavTua()
    print(f"{oaTa.si}:{oaTa.ia}")
    print(f"{oaTo.si}:{oaTo.ia}")
    print(f"{obTa.zavTu}\n")
    i0 = 0
    while i0 < obTa.iTr - 2:
        s_z = obTa.zavTu[i0:i0+3]
        Luza.append(daaT[s_z])
        i0 += 1
    i1 = 0
    iLen_z = len(Luza)
    while i1 < iLen_z:
        print(f"{Luza[i1]} ")
        i1 += 1
#--------------------------
def ua_kixj_Ta():
    oaTa = oa(si="adaLao")
    oaTa.uiaa(oaTa.si)
    oaTo = oa(si="sunisamgu")
    oaTo.uiaa(oaTo.si)
    obTa = ob(oaTa, oaTo)
    obTa.iTr = 200000
    obTa.uzavTua()
    #-----------
    oac = oc(so=ob.sopapi)
    fia = open("qevce_asu_zave.so25.11cab.txt", 'r')
    oac.La = fia.readlines()
    fia.close()
    print(len(oac.La))
    oac.La = [s_ for s_ in oac.La if s_[0] not in " #-"]
    print(len(oac.La))
    oac.Lb = []
    for s_ in oac.La:
        L_ = s_.split()
        for sa in L_:
            oac.Lb.append(sa)
    print(len(oac.Lb)) 
    
    oac.Lc = []
    i0 = 0
    while i0 < obTa.iTr - 2 and len(oac.Lc) < 25**3:
        s_a = obTa.zavTu[i0:i0+3]
        if s_a not in oac.Lc:
            oac.Lc.append(s_a)
        i0 += 1
    print(f"{i0}:{len(oac.Lc)}\n")
    
    #-----------
    i0 = 0
    iLenz = len(oac.Lb)
    i1 = 0
    fua = open(f"{oaTa.si}_{oaTo.si}.txt", "w")
    while i0 < 15625:
        i_ = i1 % iLenz
        s_f = f"{oac.Lc[i0]}:{oac.Lb[i_]}\n"
        fua.write(s_f)
        i0 += 1
        i1 += 1
    fua.close()
    
    #-----------
#--------------------------
def ua_kixj():
    print("uL da suni moL\n")
    oaz = oa()
    LimoL = ['ashera', 'saTan', 'ozazL', 'Toqasi']
    oca = oc(so=ob.sopapi)
    oca.da = {}
    for moL in LimoL:
        oca.da[moL] = oaz.uiaa(moL)
    print(oca.da)
    #----
    fua = open('usaTana_kixj.json', 'w')
    json.dump(oca.da, fua)
    fua.close()
    #---
    oca.db = {}
    fia = open('usaTana_kixj.json', 'r')
    oca.db = json.load(fia)
    fia.close()
    print(oca.db)
    #----

#--------------------------
if __name__=='__main__':
    ua_kixj_ka()