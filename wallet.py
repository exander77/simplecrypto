import sys, hashlib
B = 'big'; B58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
class ECC:
    def __init__(P, x, y, p): P.x = x; P.y = y; P.p = p
    def toXY(P): return b'\x04' + P.x.to_bytes(32, B) + P.y.to_bytes(32, B)
    def toX(P):  return (b'\x03' if P.x%2==1 else b'\x02') + P.x.to_bytes(32, B)
    def __add__(P, Q):   return P.__radd__(Q)
    def __mul__(P, x):   return P.__rmul__(x)
    def __rmul__(P, x, Q = None):
        for i in range(256):
            if x & (1 << i): Q = Q + P
            P = P + P
        return Q
    def __radd__(P, Q):
        if Q is None: return P
        if P == Q: d = 2*P.x; s = pow(2*P.y%P.p, P.p-2, P.p) * (3*P.x ** 2)%P.p
        else: d = P.x+Q.x; s = pow(Q.x-P.x, P.p-2, P.p) * (Q.y-P.y)%P.p
        x = (s ** 2-d) % P.p; y = (s*(P.x-x)-P.y)%P.p; return ECC(x, y, P.p)
G = ECC(p = 2**256-2**32-977, x = 0x3b78ce563f89a0ed9414f5aa28ad0d96d6795f9c63,
    y = 0xc0c686408d517dfd67c2367651380d00d126e4229631fd03f8ff35eef1a61e3c) * 2
def b58(d, r = ''): 
    while d > 0: r = B58[d % 58] + r; d = d // 58
    return r
def sha256(d):    h = hashlib.new('sha256');    h.update(d); return h.digest()
def ripemd160(d): h = hashlib.new('ripemd160'); h.update(d); return h.digest()
def bytes2wif(p): return b58(int.from_bytes(p + sha256(sha256(p))[:4], B))
def pub2addr(s):  return '1' + bytes2wif(b'\x00' + ripemd160(sha256(s)))
if (len(sys.argv) < 2 or len(sys.argv[1]) != 64):
    sys.stderr.write('Private key argument required as 64 hex characters!\n')
    sys.exit(1)
a = sys.argv[1]; b = bytes.fromhex(a); d = int.from_bytes(b, B); P = G * d
print('Private key                        : %s' % a)
print('Private key in Wif                 : %s' % bytes2wif(b))
print('Address from full public key       : %s' % pub2addr(P.toXY()))
print('Address from compressed public key : %s' % pub2addr(P.toX()))
