# sources: https://crypto.stackexchange.com/questions/13166/method-to-calculating-e-in-rsa, https://docs.python.org/3/library/random.html
import random
import math

def is_prime(n):
    # check if the number is less than 2
    if n < 2:
        return False
    # check for factors from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_random_prime(nbits):
    while True:
        # Generate a random number with nbits
        p = random.getrandbits(nbits)
        
        if is_prime(p):
            return p

# generate two random prime numbers p and q that are _
def generate_random_primes():
    p = get_random_prime(20)
    q = get_random_prime(20)
    # make sure p and q are not the same number
    while p == q:
        q = get_random_prime(20)
    return p, q  

# encrypt the message using the public key (e, n)
def rsa_encrypt(message, e, n):
     cipher_text = []
     for char in message:
        cipher_text.append(pow(ord(char), e, n))
     return cipher_text

# decrypt the cipher text using the private key (d, n)
def rsa_decrypt(cipher_text, d, n):
    decrypted_message = ""
    for char in cipher_text:
        decrypted_message += chr(pow(char, d, n))
    return decrypted_message

def main():
    # get user input for the message to be encrypted
    message = input("Enter message: ")

    p,q = generate_random_primes()
    # Calculate the value of n
    n = p * q
    # Calculate the value of phi
    phi = (p-1) * (q-1)
    # many sources suggest using 65537 as the value of e
    e = 65537
    # Calculate d using the modular inverse of e mod phi
    d = pow(e, -1, phi)

    # encrypt the message using the rsa_encrypt function and then decrypt it using the rsa_decrypt function
    cipher_text = rsa_encrypt(message, e, n)
    decrypted_message = rsa_decrypt(cipher_text, d, n)

    # print the values of p, q, e, d, cipher text, and decrypted message
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"e: {e}")
    print(f"d: {d}")
    print(f"Cipher text: {cipher_text}")
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
	main()