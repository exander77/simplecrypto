import hashlib, sys as S; T=' %s'; U=('%32s : %s\n'*5)[:-1];Y=b'\x80';X=b'\x01'
A='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'; s=input(); ####
class EC: # Secp256k1 # !!! WARNING ! THIS WALLET GENERATOR IS EXPERIMENTAL !!!
    def __init__(P, x, y, p): P.x=x; P.y=y; P.p=p # Long live Satoshi Nakamoto.
    def toXY(P): return b'\x04'+P.x.to_bytes(32, B)+P.y.to_bytes(32, B)  # 2021
    def toX(P): return (b'\x03' if P.x%2==1 else b'\x02')+P.x.to_bytes(32, B) #
    def __add__(P, Q): return P.__radd__(Q)#╔═════════════════════════════════╗
    def __mul__(P, x): return P.__rmul__(x)#║──╦╩╩═╩╩══╗───── SimpleCrypto ───║
    def __rmul__(P, x, Q=None):            #║──╣─╔═══╗─║─ wallet.py ── v1.5 ──║
        for i in range(256): # Montgomery  #║──║─╚═══╝─╚╗─ for BitCoin (BTC) ─║
            if x&(1<<i): Q=Q+P   # ladder  #║──║─╔════╗─║─────────────────────║
            P=P+P # scalar multiplication. #║──╣─╚════╝─║──── by eXander77 ───║
        return Q  # The Times 03/Jan/2009  #║──╩╦╦═╦╦═══╝─── exander77@pm.me ─║
    def __radd__(P, Q):  # In memory of #  #║github.com/exander77/simplecrypto║
        if Q is None: return P # Hal #     #╚═════════════════════════════════╝
        if P==Q: d= 2*P.x; s= pow(2*P.y % P.p, P.p-2, P.p) * (3*P.x ** 2) % P.p
        else: d= P.x+Q.x; s= pow(Q.x-P.x, P.p-2, P.p) * (Q.y-P.y) % P.p  # 4FNI
        x= (s ** 2-d) % P.p; return EC(x, (s*(P.x-x)-P.y) % P.p, P.p)   # !2KNI
def h(d, h='sha256'): h=hashlib.new(h); h.update(d); return h.digest()   # Hash
def f(d): return f(d//58)+A[d%58] if d>0 else ''  # Base58 pure integer variant 
def e(d): return '1'+e(d[1:]) if d[0]==0 else f(int.from_bytes(d, B))  # Base58
def w(p): return e(p+h(h(p))[:4]); # WIF    # Dedicated to Ledger leak victims.
def a(s): return w(b'\x00'+h(h(s), 'ripemd160'))  # Hash public key to address.
if len(s)!=64: S.exit('Usage: python3'+T*3%(S.argv[0],'<'*3,h(X).hex()))  # ERR
B='big';b=bytes.fromhex(s);d=int.from_bytes(b,B);V='Private key';W='Address'  #
P=EC(y=0xc0c686408d517dfd67c2367651380d00d126e4229631fd03f8ff35eef1a61e3c,   ##
    x=0x3b78ce563f89a0ed9414f5aa28ad0d96d6795f9c63, p=2**256-2**32-977)*2*d   #
print(U%('%s (HEX)'%V,s,'%s (WIF XY)'%V,w(Y+b),'%s (WIF X)'%V,w(Y+b+X),   # OUT
    '%s (XY)'%W,a(P.toXY()),'%s (X)'%W,a(P.toX())))  # 1 DOGE = 1 DOGE   # QED.
