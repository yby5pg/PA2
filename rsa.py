import random
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n//2 + 1, 2):
        if n % i == 0: # check for factors
            return False
    return True

def random_prime(max_value):
    while True:
        num = random.randint(2, max_value)
        if is_prime(num):
            return num

def mod_inverse(e, phi):
    # find 'd' such that (d * e) % phi = 1
    # rsa will find e given d
    def extended_gcd(a, b):
        # find gcd of a and b but where x, y are coefficients such that ax + by = gcd
        if a == 0:
            return b, 0, 1 # if a is 0, b is gcd
        
        gcd, x1, y1 = extended_gcd(b % a, a) # divide b by a and get the GCD of (b % a) and a
        # use as coefficients for the sub problem
        
        # calculate coefficients for our current problem size
        x = y1 - (b // a) * x1
        y = x1
        
        return gcd, x, y

    # get gcd and coefficients
    gcd, x, _ = extended_gcd(e, phi)
    
    # mod inverse only exists if e and phi are coprime (their GCD is 1)
    if gcd != 1:
        raise ValueError("No modular inverse exists.")
    
    # find if mod inverse is in the range [0, phi-1]
    return x % phi

def main():
    M = input("Enter the message to encrypt: ")
    
    max_value = 1000000
    p = random_prime(max_value)
    q = random_prime(max_value)
    while p == q:  # Ensure p and q are different
        q = random_prime(max_value)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 65537 # random exponent to use (prime)
    while math.gcd(e, phi) != 1:
        e = random.randrange(3, phi, 2)
    
    d = mod_inverse(e, phi)

    print(f"p: {p}")
    print(f"q: {q}")
    print(f"e: {e}")
    print(f"d: {d}")
    
    message_nums = [ord(char) for char in M]
    
    ciphertext = []
    for m in message_nums:
        # c = m^e mod n
        c = pow(m, e, n)
        ciphertext.append(c)
    
    print(f"\nCiphertext: {ciphertext}")
    
    decrypted_nums = []
    for c in ciphertext:
        # m = c^d mod n
        m = pow(c, d, n)
        decrypted_nums.append(m)
    
    decrypted = ''.join(chr(m) for m in decrypted_nums)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
