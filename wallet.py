import hashlib, sys as S;T=' %s';U=('%32s : %s\n'*6)[:-1];A='123456789ABCDEFGH'
class E: # Secp256k1 # !!! WARNING !! THIS WALLET GENERATOR IS EXPERIMENTAL !!!
    def __init__(P,x,y,p):P.x=x;P.y=y;P.p=p # Long live Satoshi Nakamoto @ 2021
    def toXY(P):return b'\x04'+P.x.to_bytes(32,B)+P.y.to_bytes(32,B) #!2KNI4FNI
    def toX(P):return (b'\x02' if P.x%2==1 else b'\x03')+P.x.to_bytes(32,B) # @
    def __add__(P,Q):return P.__radd__(Q)  #╔═════════════════════════════════╗
    def __mul__(P,x):return P.__rmul__(x)  #║──╦╩╩═╩╩══╗───── SimpleCrypto ───║
    def __rmul__(P,x,Q=None):    # 79 x 35 #║──╣─╔═══╗─║─ wallet.py ── v2.0 ──║
        for i in range(256):  # 21,000,000 #║──║─╚═══╝─╚╗─ for ₿itCoin (₿TC) ─║
            if x&(1<<i):Q+=P   # r/Bitcoin #║──║─╔════╗─║─────────────────────║
            P+=P   # The Times 03/Jan/2009 #║──╣─╚════╝─║──── by eXander77 ───║
        return Q # In memory of Hal Finney #║──╩╦╦═╦╦═══╝─── exander77@pm.me ─║
    def __radd__(P,Q):  # Vires in Numeris #║github.com/exander77/simplecrypto║
        if Q is None:return P # BlockChain #╚═════════════════════════════════╝
        if P==Q:d=2*P.x;s=pow(2*P.y%P.p,P.p-2,P.p)*(3*P.x**2)%P.p # PUMP & DUMP
        else:d=P.x+Q.x;s=pow(Q.x-P.x,P.p-2,P.p)*(Q.y-P.y)%P.p # 1 DOGE = 1 DOGE
        x=(s**2-d)%P.p;return E(x,(s*(P.x-x)-P.y)%P.p,P.p) # HODL # MOON # SAFU
h=lambda d,h='sha256':hashlib.new(h,d).digest(); g=lambda d:h(h(d),'ripemd160')
I=lambda d:I(d//58)+A[d%58] if d>0 else '';K=lambda s:W(b'\x00'+g(s));i=input()
J=lambda d:J(d//32)+[d%32] if d>0 else [];W=lambda p:M(p+h(h(p))[:4]);A+='JKLM'
M=lambda d:'1'+M(d[1:]) if d[0]==0 else I(int.from_bytes(d,B));A+='NPQRSTUVWXY'
N=lambda d:[0]+N(d[1:]) if d[0]==0 else J(int.from_bytes(d,B)); C='Private key'
l=lambda a,b,G,r:G[b]*(1&a>>b)^l(a,b+1,G,r) if b<5 else r;A+='Zabcdefghijklmno'
H=lambda h:[ord(x)>>5 for x in h]+[0]+[ord(x)&0x1f for x in h];A+='pqrstuvwxyz'
O=lambda V,G=[0x3b6a57b2,0x26508e6d,0x1ea119fa,0x3d4233dd,0x2a1462b3]: q(V,G,1)
q=lambda V,G,c:q(V[1:],G,l(c>>25,0,G,(c&2**25-1)<<5^V[0])) if len(V) else c # 4
def L(s,A='qpzry9x8gf2tvdw0s3jn54khce6mua7l',h='bc',w='1',R=range(6),t=[0]): #
    t+=N(list(g(s)));u=O(H(h)+t+[0]*6)^1 # Dedicated to Ledger leak victims.  P
    return h+w+''.join([A[d] for d in t+[(u>>5*(5-i))&0x1f for i in R]])  # T L
if len(i)!=64:S.exit('Usage: python3'+T*3%(S.argv[0],'<'*3,h(b'').hex())) # I A
a=bytes.fromhex(i);B='big';d=int.from_bytes(a,B);D='Address';X=b'\x80'+a  # M N
P=E(y=0xc0c686408d517dfd67c2367651380d00d126e4229631fd03f8ff35eef1a61e3c, # E
    x=0x3b78ce563f89a0ed9414f5aa28ad0d96d6795f9c63,p=2**256-2**32-977)*2*d  # ₿
print(U%(C+' (HEX)',i,C+' (WIF XY)',W(X),C+' (WIF X)',W(X+b'\x01'),D+' (XY)',K(
    P.toXY()),D+' (X)',K(P.toX()),D+' (SegWit Bech32)',L(P.toX())))       #QED.
