from Crypto.PublicKey import RSA
new_key = RSA.generate(1024,e=5)
pub_key = new_key.publickey().exportKey("PEM")

#opslaan en doorsturen via java

with open("public", "w") as file:
	file.write(pub_key)
	
with open("private", "w") as file:
	file.write(new_key.exportKey("PEM"))