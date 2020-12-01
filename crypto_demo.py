# pip uninstall crypto
# pip uninstall pycryptodome
# pip install pycryptodome
import os

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def getKey(password, salt=""):
    hasher = SHA256.new((password + salt).encode('utf-8'))
    print(hasher.hexdigest())
    return hasher.digest()

IV = Random.new().read(16)

salt = "kevinelong@clvrclvr.com"

#ENCRYPT
key = getKey("password", salt)
chunk = "Hello World!!!!!"
print(chunk)
encryptor = AES.new(key, AES.MODE_CBC, IV)
data = encryptor.encrypt(chunk.encode())
print(data.hex())

#DECRYPT
key = getKey("password", salt)
decryptor = AES.new(key, AES.MODE_CBC, IV)
output = decryptor.decrypt(data).decode()
print(output)
