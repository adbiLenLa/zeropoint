#11bqv_4e1:0zazL:vvs:::

# by ozazL
#john.david jones
#vanhan vaasan sairaala



dae2z = {'a': ['e', 'o'], 'b': ['p', 'p'], 'c': ['j', 'x'], 'd': ['T', 't'],
         'e': ['i', 'a'], 'f': ['h', 's'], 'g': ['k', 'q'], 'h': ['s', 'f'],
         'i': ['u', 'e'], 'j': ['x', 'c'], 'k': ['q', 'g'], 'l': ['n', 'm'],
         'm': ['L', 'n'], 'n': ['m', 'L'], 'o': ['a', 'u'], 'p': ['b', 'b'],
         'q': ['g', 'k'], 'r': ['v', 'z'], 's': ['f', 'h'], 't': ['t', 'd'],
         'u': ['o', 'i'], 'v': ['z', 'r'], 'w': ['z', 'r'], 'x': ['c', 'j'],
         'y': ['u', 'i'], 'z': ['r', 'v'], 'T': ['t', 'd'], 'L': ['n', 'm']}

daz2e = {'a': ['o', 'e'], 'b': ['p', 'p'], 'c': ['x', 'j'], 'd': ['t', 'T'],
         'e': ['a', 'i'], 'f': ['s', 'h'], 'g': ['q', 'k'], 'h': ['f', 's'],
         'i': ['e', 'u'], 'j': ['c', 'x'], 'k': ['g', 'q'], 'L': ['m', 'n'],
         'm': ['n', 'L'], 'n': ['L', 'm'], 'o': ['u', 'a'], 'p': ['b', 'b'],
         'q': ['k', 'g'], 'r': ['z', 'v'], 's': ['h', 'f'], 'T': ['d', 't'],
         't': ['T', 'd'], 'u': ['i', 'o'], 'v': ['r', 'z'], 'x': ['j', 'c'],
         'z': ['v', 'r']}

def  ue2z(sae):
  global dae2z
  suz = ''
  i0 = 0
  while i0 < len(sae):
    if sae[i0] in dae2z:
        suz += dae2z[sae[i0]][i0 % 2]
    i0 += 1
  return suz

def uz2e(saz):
  global daz2e
  sue = ""
  i0 = 0
  while i0 < len(saz):
    if saz[i0] in daz2e:
        sue += daz2e[saz[i0]][i0 % 2]
    i0 += 1
  return sue


def geTzfromi(ian):
    iexp = 1
    while 25 ** iexp <= ian:
        iexp += 1
    iexp -= 1
    so25 = "abcdefghijkLmnopqrsTtuvxz"
    iana = ian
    suz = ""
    L_i_c = []
    while iana > 0:
        i_c = iana // 25**iexp
        L_i_c.append(i_c)
        iana = iana % 25**iexp
        iexp -= 1
    if ian % 25 == 0:
        L_i_c.append(0)
    su = ""
    for i in L_i_c:
        su += so25[i]
    return su

def geTiTso25(saa):
  so25 = "abcdefghijkLmnopqrsTtuvxz"
  iLen = len(saa)
  iexp = iLen - 1
  io = 0
  for ca in saa:
    if ca in so25:
        io += so25.index(ca) * (25 ** iexp)
        iexp -= 1
  return io

def Tuadfa(x, y, n, k):
    fy = a7d((a3(y, (n-1)) + a7d(x, y)),(2.0 * a3(y, (n - 1))))
    y1 = y * (1 + a7d((fy - 1.0),k))
    return fy, y1


def geTrand10su(ifiLL, icnT, iLen):
    si0 = "0"
    Liu = ["0" for i_ in range(iLen + 0)]
    sifiLL = str(ifiLL)
    i0Len = 0
    i1cnT = 0
    while i0Len < iLen and i1cnT < icnT:
        Liu[i0Len] = sifiLL
        i0Len += 1
        i1cnT += 1
    #--
    Lrand = _urL(iLen*3, 11)
    
    Lrand = [i_ for i_ in Lrand if i_ < 10]
    i2rand = iLen
    while i0Len < iLen:
        Liu[i0Len] = str(Lrand[i2rand])
        i2rand += 1
        i0Len += 1
    siz = ""
    for c_ in Liu:
        siz += str(c_)
    su = f"{si0}.{siz}"
    
    return su

def __urL2(io):
    L_ = _urL93(io, 104, 37)
    L_ = [i_  % 2 for i_ in L_]
    return L_


def _urL2(io):
    L_ = _urL93(io, 318, 0)    
    a4 = L_[-1]%4
    if a4 == 0:
        return [0,0]
    if a4 == 1:
        return [0,1]
    if a4 == 2:
        return [1,0]
    if a4 == 3:
        return [1,1]

def _urL93(aLiTr, aLbn, bms):
    dT = datetime.today()
    dTus = dT.microsecond
    dTuT = 1000000 + bms
    LegoTa, Legoku = _a77T(aLiTr, aLbn, dTus, dTuT)
    return(Legoku)
    
def _a77Ta(aLiTr, aLbn, aLxn, aLxd):
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
                egoTa.append(aLxn)
                Lia = Lia + 1
                Lie = Lie + 1 
                if Lia == aLiTr:
                    return(egoTa, egoku)
        buS = a7(aLxn, aLxd)
        #buS = a0(buS, aLbn)
        egoku.append(buS)
        #print(f"{buS}")
        aLxn = a0(aLxn, aLxd)
        egoTa.append(aLxn)
        Lia = Lia + 1
        Lie = Lie + 1
    return(egoTa, egoku)

def geT4(i10):
    if i10 == 0:
        return "0"
    Lu4 = []
    while i10:
        Lu4.append(int(i10 % 4))
        i10 //= 4
    return ''.join(str(i_) for i_ in Lu4[::-1])