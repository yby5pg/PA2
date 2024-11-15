import random
from sympy import isprime
from math import gcd
from Crypto.Util.number import inverse

def generate_prime(limit):
    while True:
        num = random.randint(2, limit)
        if isprime(num):
            return num

def generate_keys():
    p = generate_prime(10000)  # or 1000000 for a larger prime
    q = generate_prime(10000)
    while p == q:
        q = generate_prime(10000)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Calculate d
    d = inverse(e, phi)
    
    return p, q, n, e, d

def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

def decrypt(ciphertext, d, n):
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

def main():
    message = input("Enter message: ")
    p, q, n, e, d = generate_keys()
    
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"e: {e}")
    print(f"d: {d}")
    
    ciphertext = encrypt(message, e, n)
    print("Ciphertext:", ciphertext)
    
    decrypted_message = decrypt(ciphertext, d, n)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
