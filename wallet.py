import hashwal, sys as S;N=int.from_bytes;C='Private key';D='Address';i=input()
class E: # Secp256k1 # In memory of Hal Finney. # Long live Satoshi Nakamoto. #
    def __init__(P,x,y,p):P.x=x;P.y=y;P.p=p;P.R=range(256) # HODL # The Times #
    def Y(P):return b'\x04'+P.x.to_bytes(_,B)+P.y.to_bytes(_,B) # 03/Jan/2009 #
    def X(P):return(b'\x03'if P.y%2else b'\x02')+P.x.to_bytes(_,B) # 2FNI2KNI #
    def __rmul__(P,x,Q=None):[(x&1<<i and(Q:=Q+P),P:=P+P)for i in P.R];return Q
    def __add__(P,Q):return P.__radd__(Q)#╔═══════════════════════════════════╗
    def __mul__(P,x):return P.__rmul__(x)#║─ SimpleCrypto ─ wallet.py ─ v3.0 ─║
    def __radd__(P,Q):  # Funds are SAFU. ║ github.com/exander77/simplecrypto ║
        if Q is None:return P # r/Bitcoin ╚═══════════════════════════════════╝
        if P==Q:d=2*P.x;s=pow(2*P.y%P.p,P.p-2,P.p)*3*P.x**2%P.p # PUMP & DUMP #
        else:d=P.x+Q.x;s=pow(Q.x-P.x,P.p-2,P.p)*(Q.y-P.y)%P.p # 1 DOGE = 1 DOGE
        x=(s**2-d)%P.p;return E(x,(s*(P.x-x)-P.y)%P.p,P.p) # Time for Plan ₿ ?!
h=lambda d,h='sha256':hashwal.new(h,d).digest();g=lambda d:h(h(d),'ripemd160')#
M=lambda V,A:e.join([A[d]for d in V]);I=lambda d,n:I(d//n,n)+[d%n]if d else f#L
J=lambda d,n:I(N(d,B),n)if d[0] else[0]+J(d[1:],n);K=lambda s:W(b'\x00'+g(s))#U
l=lambda a,b,G,r:G[b]*(1&a>>b)^l(a,b+1,G,r)if b<5else r;A='123456789ABCDEFGHJK'
H=lambda h:[ord(x)>>5for x in h]+[0]+[ord(x)&31for x in h];A+='LMNPQRSTUVWXYZa'
O=lambda V,G=(0x3b6a57b2,0x26508e6d,0x1ea119fa,0x3d4233dd,0x2a1462b3):q(V,G,1)#
q=lambda V,G,c:q(V[1:],G,l(c>>25,0,G,(c&2**25-1)<<5^V[0]))if len(V)else c;f=[]#
W=lambda p,A=A+'bcdefghijkmnopqrstuvwxyz':M(J(p+h(h(p))[:4],58),A);w='bc';_=32#
def L(s,A='qpzry9x8gf2tvdw0s3jn54khce6mua7l',R=range(6)):t=([0]*_+J(list(g(s)),
    _))[-33:];u=O(H(w)+t+[0]*6)^1;return w+'1'+M(t+[u>>5*(5-i)&31for i in R],A)
if len(i)!=64:S.exit('Usage: python3'+' %s'*3%(S.argv[0],'<'*3,h(b'').hex())) #
a=bytes.fromhex(i);B='big';d=N(a,B);X=b'\x80'+a;S=' (WIF X' # Too much space? #
P=E(y=0xc0c686408d517dfd67c2367651380d00d126e4229631fd03f8ff35eef1a61e3c, # BTC
    x=0x3b78ce563f89a0ed9414f5aa28ad0d96d6795f9c63,p=2**256-2**_-977)*2*d;e=''#
print(('%32s : %s\n'*6)[:-1]%(C+' (HEX)',i,C+S+'Y)',W(X),C+S+')',W(X+b'\x01'),D
    +' (XY)',K(P.Y()),D+' (X)',K(P.X()),D+' (Bech32)',L(P.X()))) # 2022 ## QED.
