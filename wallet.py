import hashlib, sys as S; T=' %s'; U=('%32s : %s\n'*6)[:-1];Y=b'\x80';X=b'\x01'
class EC: # Secp256k1 # !!! WARNING ! THIS WALLET GENERATOR IS EXPERIMENTAL !!!
    def __init__(P, x, y, p): P.x=x; P.y=y; P.p=p # Long live Satoshi Nakamoto.
    def toXY(P): return b'\x04'+P.x.to_bytes(32, B)+P.y.to_bytes(32, B)  # 2021
    def toX(P): return (b'\x02' if P.x%2==1 else b'\x03')+P.x.to_bytes(32, B) #
    def __add__(P, Q): return P.__radd__(Q)#╔═════════════════════════════════╗
    def __mul__(P, x): return P.__rmul__(x)#║──╦╩╩═╩╩══╗───── SimpleCrypto ───║
    def __rmul__(P, x, Q=None): # 79 x 37  #║──╣─╔═══╗─║─ wallet.py ── v1.7 ──║
        for i in range(256): # Montgomery  #║──║─╚═══╝─╚╗─ for BitCoin (BTC) ─║
            if x&(1<<i): Q=Q+P   # ladder  #║──║─╔════╗─║─────────────────────║
            P=P+P # scalar multiplication. #║──╣─╚════╝─║──── by eXander77 ───║
        return Q  # The Times 03/Jan/2009  #║──╩╦╦═╦╦═══╝─── exander77@pm.me ─║
    def __radd__(P, Q):  # In memory of #  #║github.com/exander77/simplecrypto║
        if Q is None: return P # Hal #  @  #╚═════════════════════════════════╝
        if P==Q: d= 2*P.x; s= pow(2*P.y % P.p, P.p-2, P.p) * (3*P.x ** 2) % P.p
        else: d= P.x+Q.x; s= pow(Q.x-P.x, P.p-2, P.p) * (Q.y-P.y) % P.p  # 4FNI
        x= (s ** 2-d) % P.p; return EC(x, (s*(P.x-x)-P.y) % P.p, P.p)   # !2KNI
hh=lambda d,h='sha256':hashlib.new(h,d).digest();w=lambda p:bb(p+hh(hh(p))[:4])
aa=lambda d,e:d.append(e) or d; ff=lambda d:aa(ff(d//32),d%32) if d>0 else [] #
g=lambda s:w(b'\x00'+hh(hh(s),'ripemd160'));A='123456789ABCDEFGHJKLMNPQRSTUVWX'
ee=lambda d:aa([0],ee(d[1:])) if d[0]==0 else ff(int.from_bytes(d,B));A+='YZab'
bb=lambda d:'1'+bb(d[1:]) if d[0]==0 else b(int.from_bytes(d,B)); h=input() # 1
b=lambda d,A=A+'cdefghijkmnopqrstuvwxyz':b(d//58)+A[d%58] if d>0 else '' # EXIT
eh=lambda h: [ord(x) >> 5 for x in h] + [0] + [ord(x) & 0x1f for x in h] # REKT
def pm(d,q=lambda a,b,G=[0x3b6a57b2,0x26508e6d,0x1ea119fa,0x3d4233dd,0x2a1462b3
    ]:G[b]*(1&a>>b),c=1): # 1 DOGE = 1 DOGE  # DO NOT GET GOXED # RIP Btc-e.com
    for v in d:t=c>>25;c=(c&2**25-1)<<5^v^q(t,0)^q(t,1)^q(t,2)^q(t,3)^q(t,4) ##
    return c; # PolyMod # SAFU # Dedicated to Ledger leak victims. # BCH SUX! #
def gg(s,A='qpzry9x8gf2tvdw0s3jn54khce6mua7l',h='bc',w='1',R=range(6)):  # SCAM
    t=[0]+ee(list(hh(hh(s),'ripemd160')));p=pm(eh(h)+t+[0]*6)^1  # SHITCOINS? #
    c=[(p>>5*(5-i))&0x1f for i in R]; return h+w+''.join([A[d] for d in t+c]) #
if len(h)!=64: S.exit('Usage: python3'+T*3%(S.argv[0],'<'*3,hh(X).hex())) # ERR
a=bytes.fromhex(h);B='big';d=int.from_bytes(a,B);V='Private key';W='Address' #H
P=EC(y=0xc0c686408d517dfd67c2367651380d00d126e4229631fd03f8ff35eef1a61e3c,   #O
    x=0x3b78ce563f89a0ed9414f5aa28ad0d96d6795f9c63,p=2**256-2**32-977)*2*d   #D
print(U%(V+' (HEX)',h,V+' (WIF XY)',w(Y+a),V+' (WIF X)',w(Y+a+X),W+' (XY)',  #L
    g(P.toXY()),W+' (X)',g(P.toX()),W+' (SegWit Bech32)',gg(P.toX())))   # QED.
