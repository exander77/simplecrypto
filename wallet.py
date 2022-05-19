import hashwal,sys as S;N=int.from_bytes;i=input();A='123456789ABCDEFG' # HODL #
class E: # Secp256k1 # Vires in Numeris:  #╔═══════════════════════════════════╗
    def __add__(P,Q):return P.__radd__(Q) #║─ SimpleCrypto ─ wallet.py ─ v3.2 ─║
    def __radd__(P,Q): # YASLU 19/Sep/2021 ║ github.com/exander77/simplecrypto ║
        if not Q:return P # Funds are SAFU ╚═══════════════════════════════════╝
        if P==Q:d=2*P.x;s=pow(2*P.y%P.p,P.p-2,P.p)*3*P.x**2%P.p# PUMP and DUMP F
        else:d=P.x+Q.x;s=pow(Q.x-P.x,P.p-2,P.p)*(Q.y-P.y)%P.p# 1 DOGE = 1 DOGE U
        x=(s**2-d)%P.p;return E(x,(s*(P.x-x)-P.y)%P.p,P.p)# Time for Plan ₿ ?! C
    def __mul__(P,x,Q=0):[(x&1<<i and(Q:=Q+P),P:=P+P)for i in P.R];return Q# MOK
    def __init__(P,x,y,p=2**256-2**32-977):P.x=x;P.y=y;P.p=p;P.R=range(256)# ON$
    def X(P):return(b'\x03'if P.y%2else b'\x02')+P.x.to_bytes(32,B)# The Times #
    def Y(P):return b'\x04'+P.x.to_bytes(32,B)+P.y.to_bytes(32,B)# 03/Jan/2009 M
h=lambda d,h='sha256':hashwal.new(h,d).digest();g=lambda d:h(h(d),'ripemd160')#O
if len(i)!=64:S.exit('Usage: python3'+' %s'*3%(S.argv[0],'<'*3,h(b'').hex())) #O
M=lambda V,A:''.join([A[d]for d in V]);I=lambda d,n:I(d//n,n)+[d%n]if d else[]#N
J=lambda d,n:I(N(d,B),n)if d[0]else[0]+J(d[1:],n);K=lambda s:W(b'\x00'+g(s))#Sat
l=lambda a,b,G,r:G[b]*(1&a>>b)^l(a,b+1,G,r)if b<5else r;C='Private key ';B='big'
H=lambda h:[ord(x)>>5for x in h]+[0]+[ord(x)&31for x in h];a=bytes.fromhex(i)#═╗
O=lambda V,G=(0x3b6a57b2,0x26508e6d,0x1ea119fa,0x3d4233dd,0x2a1462b3):q(V,G,1)#╝
q=lambda V,G,c:q(V[1:],G,l(c>>25,0,G,(c&2**25-1)<<5^V[0]))if len(V)else c;w='bc'
W=lambda p:M(J(p+h(h(p))[:4],58),A+'HJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz')
def L(s,A='qpzry9x8gf2tvdw0s3jn54khce6mua7l',R=range(6)):t=([0]*32+J(list(g(s)),
    32))[-33:];u=O(H(w)+t+[0]*6)^1;return w+'1'+M(t+[u>>5*(5-i)&31for i in R],A)
T='(WIF X';d=N(a,B);X=b'\x80'+a;P=E(0x3b78ce563f89a0ed9414f5aa28ad0d96d6795f9c63
    ,0xc0c686408d517dfd67c2367651380d00d126e4229631fd03f8ff35eef1a61e3c)*2*d#Hal
D='Address ';print(('%32s : %s\n'*6)[:-1]%(C+'(HEX)',i,C+T+'Y)',W(X),C+T+')',W(X
    +b'\x01'),D+'(XY)',K(P.Y()),D+'(X)',K(P.X()),D+'(Bech32)',L(P.X())))  # QED.
