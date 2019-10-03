from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

# Get the data to be signed
with open('message.txt','rb') as reader:
	message = reader.read()
	hashed = SHA256.new(message)

# Reading the private key to sign
private_key = RSA.import_key(open('rsa_private.pem').read())

# Signing and saving
signature = PKCS1_v1_5.new(private_key).sign(hashed)
with open('message.sig','wb') as sigfile:
	sigfile.write(signature)

# print(signature)