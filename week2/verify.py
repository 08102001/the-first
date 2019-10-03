from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

private_key = RSA.import_key(open('rsa_private.pem').read())

with open('message.txt','rb') as reader:
	message = reader.read()
hashed = SHA256.new(message)

with open('message.sig','rb') as reader:
	signature = reader.read()

verifier = PKCS1_v1_5.new(private_key)
result = verifier.verify(hashed, signature)

if result:
	print("The signature verifies for the file")
else:
	print("The signature is not valid for the file")