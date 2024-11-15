import random
from math import gcd

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 | n == 0 | n == 1:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def random_prime(limit):
    while True:
        num = random.randint(2, limit)
        if is_prime(num):
            return num

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def modinv(e, phi):
    gcd_val, x, _ = extended_gcd(e, phi)
    if gcd_val != 1:
        raise Exception('Modular inverse does not exist.')
    else:
        return x % phi

def encrypt(M, e, n):
    # converting to integers based on ASCII
    M_ints = [ord(char) for char in M]
    cipher_ints = [pow(m, e, n) for m in M_ints]
    return cipher_ints

def decrypt(cipher_ints, d, n):
    # Decrypt each integer
    decrypted_ints = [pow(c, d, n) for c in cipher_ints]
    # convert back
    decrypted = ''.join([chr(i) for i in decrypted_ints])
    return decrypted

def main():
    M = input("Enter the message to encrypt: ")

    limit = 10000
    p = random_prime(limit)
    q = random_prime(limit)

    while q == p:
        q = random_prime(limit)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = modinv(e, phi)

    # print
    print(f"\np: {p}")
    print(f"q: {q}")
    print(f"e: {e}")
    print(f"d: {d}")

    cipherText = encrypt(M, e, n)
    print(f"\nCiphertext: {cipherText}")

    decrypted = decrypt(cipherText, d, n)
    print(f"\nDecrypted message: {decrypted}")

if __name__ == "__main__":
    main()
