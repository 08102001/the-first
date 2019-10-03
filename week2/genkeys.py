from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

# Generating the public key - private key pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Saving the genrated keys in pem files
with open('rsa_private.pem', 'wb') as priv:
	priv.write(private_key)
with open('rsa_public.pem', 'wb') as pub:
	pub.write(public_key)

# Pubkey hash for the blockchain
hasher = SHA256.new()
hasher.update(public_key)
print(hasher.hexdigest())
