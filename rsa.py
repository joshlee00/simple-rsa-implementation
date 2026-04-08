import math

# generate two random prime numbers p and q that are _
def generate_random_primes():
    p = 17
    q = 11
    return p, q     

# encrypt the message using the public key (e, n)
def rsa_encrypt(message, e, n):
     message = int(message)
     cipher_text = pow(message, e, n)
     return cipher_text

# decrypt the cipher text using the private key (d, n)
def rsa_decrypt(cipher_text, d, n):
    decrypted_message = pow(cipher_text, d, n)
    return decrypted_message

def main():
    # get user input for the message to be encrypted
    message = input("Enter message: ")

    p,q = generate_random_primes()
    # Calculate the value of n
    n = p * q
    # Calculate the value of phi
    phi = (p-1) * (q-1)
    print(f"phi: {phi}")
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
