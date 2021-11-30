#https://cryptor.net/bezopasnost/diffie-hellman-protocol


import random
import math

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

class diffie_hellman(object):
    
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None
        
        
    def generate_partial_key(self):
        partial_key = self.public_key1**self.private_key
        partial_key = partial_key % self.public_key2
        
        return partial_key
    
    
    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r**self.private_key
        full_key = full_key%self.public_key2
        self.full_key = full_key
        
        return full_key
    
    
    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        
        for c in message:
            encrypted_message += chr(ord(c)+key)
            
        return encrypted_message
    
    
    def decrypt_message(self, message):
        decrypted_message = ""
        key = self.full_key
        
        for c in message:
            decrypted_message += chr(ord(c)-key)
            
        return decrypted_message



message = "Привет МИР!!!"
m = 1000
a1 = 0
a2 = 0
a3 = 0
a4 = 0

while 1:
    
    if(miller_rabin(random.randint(2, m-1),m) and not a1):
        Alisa_public_key = random.randint(2, m-1)
        print('Alisa_public_key:', Alisa_public_key)
        a1 = 1
        
    if(miller_rabin(random.randint(2, m-1),m)and not a2):
        Alisa_private_key = random.randint(2, m-1)
        print('Alisa_private_key:', Alisa_private_key)
        a2 = 1
        
    if(miller_rabin(random.randint(2, m-1),m) and not a3):
        Bob_public_key = random.randint(2, m-1)
        print('Bob_public_key:', Bob_public_key)
        a3 = 1
        
    if(miller_rabin(random.randint(2, m-1),m) and not a4):
        Bob_private_key = random.randint(2, m-1)
        print('Bob_private_key:', Bob_private_key)
        a4 = 1
        
    if(a1 and a2 and a3 and a4):
        break

Alisa = diffie_hellman(Alisa_public_key, Bob_public_key, Alisa_private_key)
Bob = diffie_hellman(Alisa_public_key, Bob_public_key, Bob_private_key)
Bob_private_key: 585
Bob_public_key: 430
Alisa_public_key: 433
Alisa_private_key: 873
Alisa_partial_key = Alisa.generate_partial_key()
print(Alisa_partial_key)

Bob_partial_key = Bob.generate_partial_key()
print(Bob_partial_key)
223
Alisa_full_key = Alisa.generate_full_key(Bob_partial_key)
print(Alisa_full_key)
303
Bob_full_key = Bob.generate_full_key(Alisa_partial_key)
print(Bob_full_key)
303
Bob_encrypted = Bob.encrypt_message(message)
print(Bob_encrypted)

message = Alisa.decrypt_message(Bob_encrypted)
print(message)