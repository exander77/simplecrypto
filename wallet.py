import hashlib, sys as S;T=' %s';U=('%32s : %s\n'*6)[:-1];Y=b'\x80';X=b'\x01' #
class EC: # Secp256k1 # !!! WARNING ! THIS WALLET GENERATOR IS EXPERIMENTAL !!!
    def __init__(P, x, y, p): P.x=x; P.y=y; P.p=p # Long live Satoshi Nakamoto.
    def toXY(P): return b'\x04'+P.x.to_bytes(32, B)+P.y.to_bytes(32, B)  # 2021
    def toX(P): return (b'\x02' if P.x%2==1 else b'\x03')+P.x.to_bytes(32, B) #
    def __add__(P, Q):return P.__radd__(Q) #╔═════════════════════════════════╗
    def __mul__(P, x):return P.__rmul__(x) #║──╦╩╩═╩╩══╗───── SimpleCrypto ───║
    def __rmul__(P, x, Q=None):  # 79 x 36 #║──╣─╔═══╗─║─ wallet.py ── v1.8 ──║
        for i in range(256):  # 21,000,000 #║──║─╚═══╝─╚╗─ for BitCoin (BTC) ─║
            if x&(1<<i):Q+=P   # r/Bitcoin #║──║─╔════╗─║─────────────────────║
            P+=P   # The Times 03/Jan/2009 #║──╣─╚════╝─║──── by eXander77 ───║
        return Q # In memory of Hal Finney #║──╩╦╦═╦╦═══╝─── exander77@pm.me ─║
    def __radd__(P, Q): # Vires in Numeris #║github.com/exander77/simplecrypto║
        if Q is None:return P # BlockChain #╚═════════════════════════════════╝
        if P==Q: d= 2*P.x; s= pow(2*P.y % P.p, P.p-2, P.p) * (3*P.x ** 2) % P.p
        else: d= P.x+Q.x; s= pow(Q.x-P.x, P.p-2, P.p) * (Q.y-P.y) % P.p  # 4FNI
        x= (s ** 2-d) % P.p; return EC(x, (s*(P.x-x)-P.y) % P.p, P.p)   # !2KNI
hh=lambda d,h='sha256':hashlib.new(h,d).digest();w=lambda p:bb(p+hh(hh(p))[:4])
k=lambda s:hh(hh(s),'ripemd160');g=lambda s:w(b'\x00'+k(s));A='123456789ABCDEF'
l=lambda a,b,G,r:G[b]*(1&a>>b)^l(a,b+1,G,r) if b<5 else r;A+='GHJKLMNPQRSTUVWX'
ee=lambda d:aa([0],ee(d[1:])) if d[0]==0 else ff(int.from_bytes(d,B));A+='YZab'
b=lambda d:b(d//58)+A[d%58] if d>0 else '';A+='cdefghijkmnopqrstuvwxyz';B='big'
eh=lambda h:[ord(x)>>5 for x in h]+[0]+[ord(x)&0x1f for x in h] # 1DOGE = 1DOGE
q=lambda V,G,c:q(V[1:],G,l(c>>25,0,G,(c&2**25-1)<<5^V[0])) if len(V) else c  #G
aa=lambda d,e:d.append(e) or d;ff=lambda d:aa(ff(d//32),d%32) if d>0 else [] #O
bb=lambda d:'1'+bb(d[1:]) if d[0]==0 else b(int.from_bytes(d,B));h=input() #DEX
pm=lambda V,G=[0x3b6a57b2,0x26508e6d,0x1ea119fa,0x3d4233dd,0x2a1462b3]:q(V,G,1)
def gg(s,A='qpzry9x8gf2tvdw0s3jn54khce6mua7l',h='bc',w='1',R=range(6)):  # REKT
    t=[0]+ee(list(k(s)));p=pm(eh(h)+t+[0]*6)^1 # PUMP & DUMP # Fontas # Btc-e #
    c=[(p>>5*(5-i))&0x1f for i in R]; return h+w+''.join([A[d] for d in t+c]) #
if len(h)!=64: S.exit('Usage: python3'+T*3%(S.argv[0],'<'*3,hh(X).hex())) # ERR
a=bytes.fromhex(h);B='big';d=int.from_bytes(a,B);V='Private key';W='Address' #H
P=EC(y=0xc0c686408d517dfd67c2367651380d00d126e4229631fd03f8ff35eef1a61e3c,   #O
    x=0x3b78ce563f89a0ed9414f5aa28ad0d96d6795f9c63,p=2**256-2**32-977)*2*d   #D
print(U%(V+' (HEX)',h,V+' (WIF XY)',w(Y+a),V+' (WIF X)',w(Y+a+X),W+' (XY)',  #L
    g(P.toXY()),W+' (X)',g(P.toX()),W+' (SegWit Bech32)',gg(P.toX())))   # QED.
