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

# Function to find the modular inverse of e
def modular_inverse(e, phi):
    # Extended Euclidean Algorithm to find the inverse
    a, b, u = 0, phi, 1
    while e > 0:
        q = b // e
        e, a, b, u = b % e, u, e, a - q * u
    if b == 1:
        return a % phi

# RSA encryption
def encrypt(message, n, e):
    return [pow(ord(char), e, n) for char in message]

# RSA decryption
def decrypt(ciphertext, n, d):
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Main function
def main():
    # Input message
    message = input("Enter the message: ")

    # Generate p and q
    p = random_prime(10000)  # Adjust if performance issues occur
    q = random_prime(10000)

    # Calculate n and phi
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) == 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Calculate d
    d = modular_inverse(e, phi)

    # Encrypt the message
    ciphertext = encrypt(message, n, e)
    print(f"Ciphertext: {ciphertext}")

    # Output values of p, q, e, and d
    print(f"p: {p}, q: {q}, e: {e}, d: {d}")

    # Decrypt the message
    decrypted_message = decrypt(ciphertext, n, d)
    print(f"Decrypted Message: {decrypted_message}")


if __name__ == "__main__":
    main()
