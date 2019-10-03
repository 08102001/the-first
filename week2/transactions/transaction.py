from Crypto.Hash import SHA256

class Transaction:
	def __init__(self):
		self._hash = ""
		self.ver = 1
		self.lock_time = 0
		self.inputs = [{"prev_out":"","n":0,"scriptsig":""}]
		self.outputs = []

	def add_input(self, trxhash, n, signature):
		self.inputs.append({"prev_out":trxhash, "n":n, "scriptsig":signature})

	def add_output(self, txvalue, script):
		self.outputs.append({"value":txvalue, "scriptPubKey":script})

	def hash_self(self):
		hinput = str(self.inputs) + str(self.outputs)
		bufr = SHA256.new(bytes(hinput, encoding='utf8'))
		self._hash = bufr.hexdigest()

	def verify_output(self):
		pass
		# Complicated algorithm which checks that the outputs values are not more than the inputs

j = Transaction()
j.add_input('trxhash', 10, 'sdkfhsdfhskjhj')
j.add_output('txvalue', 'script')
j.hash_self()
print(j._hash)
