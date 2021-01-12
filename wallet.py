import hashlib; B='big'; U=('%32s : %s\n'*4)[:-1]; V='Private key'; W='Address'
class ECC:
    def __init__(P, x, y, p): P.x = x; P.y = y; P.p = p
    def toXY(P): return b'\x04' + P.x.to_bytes(32, B) + P.y.to_bytes(32, B)
    def toX(P): return (b'\x03' if P.x%2==1 else b'\x02') + P.x.to_bytes(32, B)
    def __add__(P, Q): return P.__radd__(Q)
    def __mul__(P, x): return P.__rmul__(x)
    def __rmul__(P, x, Q = None):
        for i in range(256):
            if x & (1 << i): Q = Q + P
            P = P + P
        return Q
    def __radd__(P, Q):
        if Q is None: return P
        if P == Q: d = 2*P.x; s = pow(2*P.y%P.p, P.p-2, P.p) * (3*P.x ** 2)%P.p
        else: d = P.x+Q.x; s = pow(Q.x-P.x, P.p-2, P.p) * (Q.y-P.y)%P.p
        x = (s ** 2-d) % P.p; return ECC(x, (s*(P.x-x)-P.y)%P.p, P.p)
G = ECC(p = 2**256-2**32-977, x = 0x3b78ce563f89a0ed9414f5aa28ad0d96d6795f9c63,
    y = 0xc0c686408d517dfd67c2367651380d00d126e4229631fd03f8ff35eef1a61e3c) * 2
def g(d, r, A = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'): 
    while d > 0: r = A[d % 58] + r; d = d // 58;
    return r
def h(d, h='sha256'): h = hashlib.new(h); h.update(d); return h.digest()
def bts2wif(q, p): return q + g(int.from_bytes(p + h(h(p))[:4], B), '')
def pub2addr(s): return bts2wif('1', b'\x00' + h(h(s), 'ripemd160'))
a = input(); b = bytes.fromhex(a); d = int.from_bytes(b, B); P = G * d
print(U%('%s (HEX)'%V, a, '%s (WIF)'%V, bts2wif('', b), '%s (XY)'%W, 
    pub2addr(P.toXY()), '%s (X aka Compressed)'%W, pub2addr(P.toX())))
