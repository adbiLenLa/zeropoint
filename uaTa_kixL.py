#
#   11caf_4xL:0zazL:vvs:::
#   kakacaf_kixL
#
#   jones.john.david@gmail.com
#--------------------------
exec(open("koLa_kixpu.py").read())
#--------------------------
def ua_kixL_Ta():
    print("jesus qazuhat")
#--------------------------

def ua_kixn():
    fia = open("Lisa_Lisb.txt")
    Lisaa = fia.readlines()
    fia.close()
    print(Lisaa[0:10])
    Luza = []
    Luzb = []
    i0 = 0
    while i0 < len(Lisaa):
        L_ = Lisaa[i0].split(':')
        Luza.append(L_[0])
        Luzb.append(L_[1])

        i0 += 1
    
    print(len(Luza), len(Luzb))
    #print(Luza[0:10])
    i1 = 0
    Luza_sa = []
    Luzb_sa = []
    for s_za in Luza:
        L_ = s_za.split()
        for s_ in L_:
             Luza_sa.append(s_)

    for s_zb in Luzb:
        L_ = s_zb.split()
        for s_ in L_:
             Luzb_sa.append(s_)
    #---
    print(len(Luza_sa), len(Luzb_sa))
    #print(Luza_sa[0:13])
    #--------------
    fua = open("Lisa_Lisb_Lofdiz_11cah.txt", "w")
    i0 = 0
    while i0 < len(Luzb_sa):
        fua.write(f"{Luza_sa[i0]}:{Luzb_sa[i0]}\n") 
        i0 += 1
    fua.close()

#--------------------------
def ua_kixL():
    print("siso uamu unefdiLuLku\n")
    fia = open("qevce_asu_zave.english.11ca6.txt", "r")
    Lisa = fia.readlines()
    fia.close()
    Lisa = [s_.strip() for s_ in Lisa]
    Luza = []
    s__ = " #-"
    Lisa = [s_ for s_ in Lisa if len(s_) > 0 and s_[0] not in s__ ]
    for sa in Lisa:
        L_ = sa.split()
        for s_ in L_:
            Luza.append(s_)
        
    print(len(Luza))
    #---------------------
    fib = open("qevce_asu_zave.so25.11cab.txt")
    Lisb = fib.readlines()
    fib.close()
    Lisb = [s_.strip() for s_ in Lisb]
    Luzb = []
    Lisb = [s_ for s_ in Lisb if len(s_) > 0 and s_[0] not in s__ ]
    for sb in Lisb:
            L_ = sb.split()
            for s_ in L_:
                Luzb.append(s_)
    print(len(Luzb))
    print(f"len(Lisa): {len(Lisa)}\nlen(Lisb): {len(Lisb)}\n")
    #----
    print(Lisb[-2])
    print(Lisa[-2])
    #--------------
    fua = open("Lisa_Lisb.txt", "w")
    i0 = 0
    while i0 < len(Lisa):
         fua.write(f"{Lisa[i0]}:{Lisb[i0]}\n")
         i0 += 1
    fua.close()
    #-------------
    i1 = 0
    
#--------------------------
if __name__ == '__main__':
    ua_kixL()
    ua_kixn()