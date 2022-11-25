import numpy as np

message = "This is a message."

def encrypt(message, key, _filler_char='-'):
	message = message.replace(" ", '')
	message = message.lower()

	#TODO: Get size
	# where size **2 >= len(message)
	# 1 opt is to find nearst square number
	# else ex 18 -> 6 and 3
	c = len(key)
	r = c
	
	# Initialise Cipher
	m = np.chararray(r*c) # as list first to assign
	m[:] = _filler_char # for empty  elements
	
	# Populate cipher
	for i in range(len(message)):
		m[i] = message[i]

	
	# From list to matrix
	m.shape = (r,c)


	# Get list of ints from string key
	keychain = [int(c) for c in key]

	# Init Cipher
	cipher = np.chararray((r,c))
	
	# Populate cipher
	i = 0
	for k in keychain:
		cipher[:,i] = m[:,k-1] # cipher's ith column = m's k-1 th column
		i += 1


	ciphertext = cipher.tobytes().decode("utf-8")
	return ciphertext
