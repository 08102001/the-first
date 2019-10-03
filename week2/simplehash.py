from Crypto.Hash import SHA256

with open('rsa_public.pem','rb') as red:
	message = red.read()

hasher = SHA256.new(message)
PUBKEY_HASH = hasher.hexdigest()
print(PUBKEY_HASH)
# Encode this in base58 for public use