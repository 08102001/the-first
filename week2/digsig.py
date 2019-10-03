from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

with open('message.txt','rb') as reader:
	message = reader.read()

private_key = RSA.import_key(open('rsa_private.pem').read())
hashed = SHA256.new(message)

signature = PKCS1_v1_5.new(private_key).sign(hashed)

with open('message.sig','wb') as sigfile:
	sigfile.write(signature)

print(signature)