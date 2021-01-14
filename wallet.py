import hashlib, sys as S; T=' %s'; U=('%32s : %s\n'*6)[:-1];Y=b'\x80';X=b'\x01'
A='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'; h=input(); ####
class EC: # Secp256k1 # !!! WARNING ! THIS WALLET GENERATOR IS EXPERIMENTAL !!!
    def __init__(P, x, y, p): P.x=x; P.y=y; P.p=p # Long live Satoshi Nakamoto.
    def toXY(P): return b'\x04'+P.x.to_bytes(32, B)+P.y.to_bytes(32, B)  # 2021
    def toX(P): return (b'\x02' if P.x%2==1 else b'\x03')+P.x.to_bytes(32, B) #
    def __add__(P, Q): return P.__radd__(Q)#╔═════════════════════════════════╗
    def __mul__(P, x): return P.__rmul__(x)#║──╦╩╩═╩╩══╗───── SimpleCrypto ───║
    def __rmul__(P, x, Q=None): # 79 x 29  #║──╣─╔═══╗─║─ wallet.py ── v1.6 ──║
        for i in range(256): # Montgomery  #║──║─╚═══╝─╚╗─ for BitCoin (BTC) ─║
            if x&(1<<i): Q=Q+P   # ladder  #║──║─╔════╗─║─────────────────────║
            P=P+P # scalar multiplication. #║──╣─╚════╝─║──── by eXander77 ───║
        return Q  # The Times 03/Jan/2009  #║──╩╦╦═╦╦═══╝─── exander77@pm.me ─║
    def __radd__(P, Q):  # In memory of #  #║github.com/exander77/simplecrypto║
        if Q is None: return P # Hal #     #╚═════════════════════════════════╝
        if P==Q: d= 2*P.x; s= pow(2*P.y % P.p, P.p-2, P.p) * (3*P.x ** 2) % P.p
        else: d= P.x+Q.x; s= pow(Q.x-P.x, P.p-2, P.p) * (Q.y-P.y) % P.p  # 4FNI
        x= (s ** 2-d) % P.p; return EC(x, (s*(P.x-x)-P.y) % P.p, P.p)   # !2KNI
def hh(d, h='sha256'): return hashlib.new(h,d).digest()  # Hashlib hash wrapper
def b(d): return b(d//58)+A[d%58] if d>0 else ''  # Base58 pure integer variant 
def bb(d): return '1'+bb(d[1:]) if d[0]==0 else b(int.from_bytes(d,B)) # Base58
def w(p): return bb(p+hh(hh(p))[:4]); # WIF # Dedicated to Ledger leak victims.
def g(s): return w(b'\x00'+hh(hh(s),'ripemd160')) # Hash public key to address.
if len(h)!=64: S.exit('Usage: python3'+T*3%(S.argv[0],'<'*3,hh(X).hex())) # ERR
B='big';a=bytes.fromhex(h);d=int.from_bytes(a,B);V='Private key';W='Address'  #
P=EC(y=0xc0c686408d517dfd67c2367651380d00d126e4229631fd03f8ff35eef1a61e3c,   ##
    x=0x3b78ce563f89a0ed9414f5aa28ad0d96d6795f9c63, p=2**256-2**32-977)*2*d   #
def aa(d, e): d.append(e); return d; # Append helper # 1 DOGE = 1 DOGE = 1 DOGE
def ff(d): return aa(ff(d//32),d%32) if d>0 else []  # Base32 with array result
def ee(d): return aa([0],ee(d[1:])) if d[0]==0 else ff(int.from_bytes(d,B))
def eh(h): return [ord(x) >> 5 for x in h] + [0] + [ord(x) & 0x1f for x in h]
def pm(d, g=[0x3b6a57b2,0x26508e6d,0x1ea119fa,0x3d4233dd,0x2a1462b3], c=1):
    for v in d:
        t= c>>25; c= (c&0x1ffffff)<<5^v;
        for i in range(5): c^= g[i] if ((t>>i)&1) else 0
    return c
def gg(s, A='qpzry9x8gf2tvdw0s3jn54khce6mua7l', h='bc', w='1', R=range(6)):
    t= [0]+ee(list(hh(hh(s),'ripemd160'))); p= pm(eh(h)+t+[0]*6)^1 # Bech32  #?
    c= [(p>>5*(5-i))&0x1f for i in R]; return h+w+''.join([A[d] for d in t+c])
print(U%(V+' (HEX)',h,V+' (WIF XY)',w(Y+a),V+' (WIF X)',w(Y+a+X),W+' (XY)', 
    g(P.toXY()),W+' (X)',g(P.toX()),W+' (SegWit Bech32)',gg(P.toX())))   # QED.
