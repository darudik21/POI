

 
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
# import binascii
 
# keyPair = RSA.generate(3072)
 
# pubKey = keyPair.publickey()
# print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
# pubKeyPEM = pubKey.exportKey()
# print(pubKeyPEM.decode('ascii'))
 
# print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
# privKeyPEM = keyPair.exportKey()
# print(privKeyPEM.decode('ascii'))
 
# #encryption
# msg = 'A message for encryption'
# encryptor = PKCS1_OAEP.new(pubKey)
# encrypted = encryptor.encrypt(msg)
# print("Encrypted:", binascii.hexlify(encrypted))


import random
import math
def RSA(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    e = 0
    for i in range(2, z):
        if math.gcd(i, z) == 1:
            e = i
            break
    d = 0
    for i in range(z):
        x = 1+(i*z)
        if x % e == 0:
            d = int(x / e)
            break
    return [e, n], [d, n]
def get_prime_number():
    while True:
        number = random.randint(111, 999)
        if  miller_rabin(number,10000) is True: 
            return number
def power(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res
def miller_rabin(n, k):

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    
    while s % 2 == 0:
        r += 1
        s //= 2
        
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        
        if x == 1 or x == n - 1:
            continue
            
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
        
    return True
def encrypt(text, key):
    encrypt_text = []
    for m in text:
        encrypt_text.append(pow(ord(m), key[0]) % key[1])
    return encrypt_text
def decrypt(text, key):
    decrypt_text = ''
    for m in text:
        decrypt_text += chr(pow(m, key[0]) % key[1])
    return decrypt_text
public_key, private_key = RSA(get_prime_number(), get_prime_number())

print('Public Key:', public_key)
print('Private Key:', private_key)

text = input("Введите текст, который хотите зашифровать: ")
encrypted_text = encrypt(text, public_key)
print("Encrypted text: ", encrypted_text)

decrypted_text = decrypt(encrypted_text, private_key)
print('Decrypted text:', decrypted_text)