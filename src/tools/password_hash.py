from os import urandom
from hashlib import scrypt
from base64 import b64encode, b64decode

def get_password_hash(password):
        password_binary_hash = scrypt(password.encode(),salt=urandom(16),n=128,r=8,p=1)
        return b64encode(password_binary_hash).decode()

def verify_password_hash(password, hash):
        #TODO
        pass