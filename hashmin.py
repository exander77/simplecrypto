C=len;_32,_30=2**32,2**30;_=_32-1;Q=lambda n,d,U:int(n**(1/d)*U);F0=lambda x,y,z:z^x&(y^z)
F1=lambda x,y,z:x&y|x&z|y&z;F2=lambda x,y,z:x^y^z;F3=lambda x,y,z:F0(z,x,y) #  HASH MIN  #
F4=lambda x,y,z:y^(x|~z);F5=lambda x,y,z:F4(x,z,y);F6=lambda x,y,z:F4(y,x,z) #  LIBRARY  #
E=['big','little'];B=lambda v,b,e=0:v.to_bytes(b,E[e]);L=lambda x,y=0:(x<<y|(x&_)>>32-y)&_
I=lambda v,e=0,:int.from_bytes(v,E[e]);R=lambda x,y,s=0:((x&_)>>y|x<<32+s-y)&_32-1;G=range
def S(N,M):S=set();P=[n for n in G(2,N)if not(n in S,S.update(G(n*n,N,n)))[0]];return M(P)
class ripemd160: # Hans Dobbertin, Antoon Bosselaers and Bart Preneel 1992 (1996) ## BASED
    def __init__(S,m=0):S.c=0;S.C=b'';S.h=S.H[:];S.update(m)if m else 0 # hashmin.py  v1.0
    def digest(S):S.update(S.P(S.c));return b''.join([B(i,4,S.E)for i in S.h])
    def update(S,m):  # Hashlib compatible interface with update and digest methods. Nice?
        S.C+=m;S.c+=C(m);X=lambda W,i,j,F,a,b,c,d,k,U,m:L(a+k+F[j](b,c,d)+W[m]&_,U[i]) # ₿
        while C(S.C)>=64:S._B([I(S.C[:64][i:i+4],S.E)for i in G(0,256,4)],X);S.C=S.C[64:]#
    def P(S,l):return b'\x80'+(b'\x00'*(119-l&63))+B(l<<3,8,S.E) # Merkle–Damgård padding.
    K,L=S(8,lambda P:([0]+[Q(n,2,_30)for n in P],[Q(n,3,_30)for n in P]+[0]));M=[0]*80;E=1
    N=M[:];F=[F2,F0,F5,F3,F6];X=lambda X,n:[7,4,13,1,10,6,15,3,12,0,9,5,2,14,11,8][X[n]] #
    H=[0x67452301,0xEFCDAB89,0x98BADCFE,0x10325476,0xC3D2E1F0] # Initialization vector IV.
    for i in G(80):M[i],N[i]=(i,i*9+5&15)if i<16else(X(M,i-16),X(N,i-16))
    U=(11,14,15,12,5,8,7,9,11,13,14,15,6,7,9,8,7,6,8,13,11,9,7,15,7,12,15,9,11,7,13,12,
        11,13,6,7,14,9,13,15,14,8,13,6,5,12,7,5,11,12,14,15,14,15,9,8,9,14,5,6,8,6,5,12,
        9,15,5,11,6,8,13,12,5,12,13,14,11,8,5,6);V=(8,9,9,11,13,15,15,5,7,7,8,11,14,14,12,
        6,9,13,15,7,12,8,9,11,7,7,12,7,6,15,13,11,9,7,15,11,8,6,6,14,12,13,5,14,13,13,7,5,
        15,5,8,11,14,14,6,14,6,9,12,9,12,5,15,8,8,5,12,9,12,5,14,6,8,13,6,5,15,13,11,11)
    def _B(S,W,X,Z=G(80)):  # Anybody knows where are the values from U and V coming from?
        a,b,c,d,e=S.h;v,w,x,y,z=S.h
        for i in Z: # Aaron Swartz & Edward Snowden & Julian Assange & Satoshi Nakamoto
            a,e,d,c,b=e,d,L(c,10),b,e+X(W,i,j:=i>>4,S.F,a,b,c,d,S.K[j],S.U,S.M[i])
            v,z,y,x,w=z,y,L(x,10),w,z+X(W,i,j,S.F[::-1],v,w,x,y,S.L[j],S.V,S.N[i])
        S.h=[x+y+z&_ for(x,y,z)in zip(S.h[1:]+S.h[:1],(c,d,e,a,b),(y,z,v,w,x))]
class md4(ripemd160): # Created by Ronald Rivest 1990, described in RFC1320.
    M=list(G(16))+[i%15for i in G(0,57,4)]+[15,0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
    K=[0,Q(2,2,_30),Q(3,2,_30)];U=[3,7,11,19]*4+[3,5,9,13]*4+[3,9,11,15]*4;F=[F0,F1,F2]
    def _B(S,W,X,Z=G(48)): # Hal Finney
        a,b,c,d=S.h[:4] # Do you know what is the difference between a government employee?
        for i in Z:j=i>>4;a,d,c,b=d,c,b,X(W,i,j,S.F,a,b,c,d,S.K[j],S.U,S.M[i])
        S.h=[x+y&_ for(x,y)in zip(S.h,(a,b,c,d))] # and a BitCoin miner?    Proof of work.
class md5(md4): # Created by Ronald Rivest 1992, described in RFC1321.
    K=[int(_32*abs((2.718281828459**((i+1)*1j)).imag))for i in G(64)];F=[F0,F3,F2,F4]
    U=[7,12,17,22]*4+[5,9,14,20]*4+[4,11,16,23]*4+[6,10,15,21]*4;M,A=[1,5,3,7],[0,1,5,0]
    def _B(S,W,X,Z=G(64)): # First MD5 colission: 79054025255fb1a26e4bc422aef54eb4
        a,b,c,d=S.h[:4] # How many Borgs do you need to change a light bulb? All of them.
        for i in Z:j=i>>4;a,d,c,b=d,c,b,b+X(W,i,j,S.F,a,b,c,d,S.K[i],S.U,S.M[j]*i+S.A[j]&15)
        S.h=[x+y&_ for(x,y)in zip(S.h,(a,b,c,d))]   
class sha0(ripemd160): # National Security Agency 1993
    E=0;K=md4.K[1:]+[Q(5,2,_30),0xCA62C1D6];F=[F0,F2,F1,F2];D=0
    def _B(S,W,X,Y=G(16,80),Z=G(80)):
        W+=[0]*64;a,b,c,d,e=S.h
        for i in Y:W[i]=L(W[i-3]^W[i-8]^W[i-14]^W[i-16],S.D)
        for i in Z:j=i//20;e,d,c,b,a=d,c,L(b,30),a,L(a,5)+S.F[j](b,c,d)+e+S.K[j]+W[i]
        S.h=[x+y&_ for(x,y)in zip(S.h,(a,b,c,d,e))]
class sha1(sha0):D=1 # National Security Agency 1995. Just a rotation added to SHA-0.
class sha256(ripemd160): # National Security Agency 2001
    E=0;H,K=S(312,lambda P:([Q(n,2,_32)for n in P[:8]],[Q(n,3,_32)for n in P]))
    def _B(S,W,X,Y=G(48),Z=G(64),R=lambda x,a,b,c,s=32:R(x,a)^R(x,b)^R(x,c,s)):
        a,b,c,d,e,f,g,h=S.h
        for i in Y:x,y=W[i+1],W[i+14];W[i+16]=W[i]+R(x,7,18,3)+W[i+9]+R(y,17,19,10)
        for i in Z: # Do you know what C in NSA means? Constitution... 
            t=h+R(e,6,11,25,0)+(e&f^~e&g)+S.K[i]+W[i]
            h,g,f,e,d,c,b,a=g,f,e,d+t&_,c,b,a,t+R(a,2,13,22,0)+(a&b^a&c^b&c)
        S.h=[x+y&_ for(x,y)in zip(S.h,(a,b,c,d,e,f,g,h))] # Extreme programming FTW.
def new(h,d):return{'md5':md5,'ripemd160':ripemd160,'sha1':sha1,'sha256':sha256}[h](d) # .
