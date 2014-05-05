from Crypto.PublicKey import RSA
import sys
from base64 import b64decode

cmd = "BPiQRVcW5mwZM3/Kba7IlLsHpZuZJtBoGH1bssMu1y3L4IL1PK5/IA=="


key=open("private", "r").read()
priv_key = RSA.importKey(key)
plaintext=priv_key.decrypt(b64decode(cmd))

with open("result", "w") as file:
	file.write(plaintext)