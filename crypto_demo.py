# pip uninstall crypto
# pip uninstall pycryptodome
# pip install pycryptodome
import os

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

IV = Random.new().read(16)

#ENCRYPT
key = getKey("secret")
chunk = "Hello World!!!!!"
encryptor = AES.new(key, AES.MODE_CBC, IV)
data = encryptor.encrypt(chunk.encode())
print(data)

#DECRYPT
key = getKey("secret")
decryptor = AES.new(key, AES.MODE_CBC, IV)
output = decryptor.decrypt(data)
print(output)
