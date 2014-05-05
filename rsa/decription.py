from Crypto.PublicKey import RSA
import sys
from base64 import b64decode

cmd = open("encrypted", "r").read()


key=open("private", "r").read()
priv_key = RSA.importKey(key)
plaintext=priv_key.decrypt(b64decode(cmd))

with open("result", "w") as file:
	file.write(plaintext)