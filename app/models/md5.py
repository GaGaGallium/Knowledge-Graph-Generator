import hashlib

def pwd_md5(password):
    password = password+'yan'
    return hashlib.md5(password.encode("utf-8")).hexdigest()