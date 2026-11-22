#
#   11cah_4xn:0zazL:vvs:::
#   kakacah_kixn
#
#   jones.john.david@gmail.com
#--------------------------
exec(open("koLa_kixpu.py").read())
#--------------------------

def ua_kixn_ka():
    LodpipaTa = Lodpipa(iboL=1)
    LodpipaTa.uefoshemia()
    Lodpipaka = Lodpipa(iboL=1)
    Lodpipaka.uefoshemia()
    #------------
    Lui = [0,0,0]
    while len(LodpipaTa.Loda) > 0:
        oda = LodpipaTa.Loda.pop()
        odb = Lodpipaka.Loda.pop()
        #-------
        print(f"{oda.cb}{oda.ca}:{odb.cb}{odb.ca}")
        #-------
        if oda.ia > odb.ia:
            Lui[0] += 1
        if odb.ia > oda.ia:
            Lui[2] += 1
        if oda.ia == odb.ia:
            Lui[1] += 1
    #------------
    print(Lui)
    #------------
#-----------------------
def ua_kixn_Ta():
    LodpipaTa = Lodpipa(iboL=1)
    i0 = 0
    LodpipaTa.uefoshemia() # shuffle
    while i0 < len(LodpipaTa.Loda):

        print(f"{LodpipaTa.Loda[i0].cb}{LodpipaTa.Loda[i0].ca}:{LodpipaTa.Loda[i0].ia}")
        i0 += 1
    #---
    print("#----------")
    od_ = LodpipaTa.Loda.pop()
    print(f"{od_.cb}{od_.ca}:{od_.ia}")
    print(f"{len(LodpipaTa.Loda)}")
#--------------------------
def ua_kixn():
    print("ozazL_buuge\n")
    #----------
    Loda = []
    sa = "HCDS"
    sb = "A23456789TJQK"
    for ca in sa:
        for cb in sb:
            idx = sb.index(cb)
            if idx >= 9:
                ia = 10
            else:
                ia = idx + 1
            Loda.append(od(sa=sa, sb=sb, ca=ca, cb=cb, ia=ia))
    #----------
    oaTa = oa()
    oaTo = oa()
    obTa = ob(oaTa, oaTo, 104)
    iTra = 104
    Lia = obTa.uvomtanLa(iTra, 16, 23)
    i0 = 0
    while i0 < iTra:
        i_a = i0 % len(Loda)
        i_b = (i0 + Lia[i0]) % len(Loda)
        Loda[i_a], Loda[i_b] = Loda[i_b], Loda[i_a]
        i0 += 1
    #----------
    for i_ in range(len(sa) * len(sb)):
        print(f"{Loda[i_].cb}{Loda[i_].ca}:{Loda[i_].ia}")
    #----------
#--------------------------
if __name__ == '__main__':
    ua_kixn_ka()