import sys
import hashlib

class Point:
    def __init__(P, x, y, p):
        P.x = x; P.y = y; P.p = p
    def __add__(P, Q):
        return P.__radd__(Q)
    def __mul__(P, x):
        return P.__rmul__(x)
    def __rmul__(P, x):
        n = P; q = None
        for i in range(256):
            if x & (1 << i):
                q = q + n
            n = n + n
        return q
    def __radd__(P, Q):
        if Q is None:
            return P
        if P == Q:
            d = 2 * P.x
            s = pow(2 * P.y % P.p, P.p-2, P.p) * (3 * P.x ** 2) % P.p
        else:
            d = P.x + Q.x
            s = pow(Q.x - P.x, P.p-2, P.p) * (Q.y - P.y) % P.p
        x = (s ** 2 - d) % P.p
        y = (s * (P.x - x) - P.y) % P.p
        return Point(x, y, P.p)
    def toBytesXY(self):
        return b'\x04' + self.x.to_bytes(32, 'big') + self.y.to_bytes(32, 'big')
    def toBytesX(self):
        return (b'\x03' if P.x%2==1 else b'\x02') + P.x.to_bytes(32, 'big')

def sha256(d):
    digest = hashlib.new('sha256'); digest.update(d)
    return digest.digest()

def ripemd160(d):
    digest = hashlib.new('ripemd160'); digest.update(d)
    return digest.digest()

def b58(d):
    if d[0] == 0:
        return '1' + b58(d[1:])
    B58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    x = sum([v * (256 ** i) for i, v in enumerate(d[::-1])])
    ret = ''
    while x > 0:
        ret = B58[x % 58] + ret
        x = x // 58
    return ret

SPEC256k1 = Point(
    x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
    y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
    p = 2**256 - 2**32 - 977
)

def bytes2wif(p):
    return b58(p + sha256(sha256(p))[:4])

def pub2addr(s):
    hash160 = ripemd160(sha256(s))
    return bytes2wif(b'\x00' + hash160)
    
if (len(sys.argv) < 2 or len(sys.argv[1]) != 64):
    sys.stderr.write('Private key argument required as 64 hex characters!\n')
    sys.exit(1)

darg = sys.argv[1]
dbytes = bytes.fromhex(darg)
print('Private key                        : %s' % darg)
print('Private key in Wif                 : %s' % bytes2wif(dbytes))
d = int.from_bytes(dbytes, 'big')
P = SPEC256k1 * d
print('Address from full public key       : %s' % pub2addr(P.toBytesXY()))
print('Address from compressed public key : %s' % pub2addr(P.toBytesX()))
