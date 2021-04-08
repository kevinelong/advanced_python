import hashlib


def hash_me(text, salt=""):
    s = text + salt
    e = s.encode()
    b = bytearray()
    b.extend(e)
    hashed = hashlib.sha3_512(e)
    result = hashed.hexdigest()

    return result


salt_source = "kevinelong"
key_salt = hash_me(salt_source)
print(key_salt)
stored_hash = hash_me("password", key_salt)

print(stored_hash)

# -----

def is_password_good(text, stored_hash):
    result = hash_me(text, key_salt)
    return stored_hash == result


fresh_password = "password"
print(is_password_good(fresh_password, stored_hash))

# HOW NOT TO DO IT
m = hashlib.md5()
data = "Welcome1!" # NO SALT
m.update(data.encode())
print(m.hexdigest())  # VERY COMMON TO FIND IN RAINBOW TABLES
