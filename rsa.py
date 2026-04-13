# sources: https://crypto.stackexchange.com/questions/13166/method-to-calculating-e-in-rsa, Gemini 3 Flash: "what value should my e be in rsa?" "how to efficiently calculate primes" "python how to convert letter to number", https://stackoverflow.com/a/8884226, https://realpython.com/ref/builtin-functions/pow/, https://docs.python.org/3/library/random.html

import math # import this module for square root function
import random # import this module to generate random numbers

def is_prime(n):
    if n < 2:
        return False
    # check for factors from 2 to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_random_prime(bits):
    while True:
        # Generate a random number that is nbits long
        p = random.getrandbits(bits)
        # make sure the number is odd, since even numbers > than 2 cannot be prime
        if p % 2 == 0:
            p += 1
        # only return the number if it is prime
        if is_prime(p):
            return p

def generate_random_primes():
    # choose 19 bits as the length of the prime number to ensure p,q are less than 1,000,000
    p = get_random_prime(19)
    q = get_random_prime(19)
    # make sure p and q are not the same number
    while p == q:
        q = get_random_prime(19)
    return p, q  

# encrypt the message using the public key (e, n)
def rsa_encrypt(message, e, n):
     cipher_text = []
     # for each character in the message, calculate the cipher text using provided formula in slides
     for char in message:
        cipher_text.append(pow(ord(char), e, n))
     return cipher_text

# decrypt the cipher text using the private key (d, n)
def rsa_decrypt(cipher_text, d, n):
    decrypted_message = ""
    # for each character in the cipher text, calculate the original character using provided formula in slides
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