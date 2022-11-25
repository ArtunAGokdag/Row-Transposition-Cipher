import numpy as np


cipher = np.chararray(4,4)
text='shtimsiaasesxeg.'

def decrypt(ciphertext, key, _filler_char='-'):

	# get array shape
	c = len(key)
	r = c
	cipher = np.chararray(r*c)

	# turn text into array
	for i in range(len(ciphertext)):
		cipher[i] = ciphertext[i]

	cipher.shape = (r,c)

	# get key
	keychain = [int(c) for c in key]

	message = np.chararray((r,c))
	
	# re order columns with key
	i = 0
	for k in keychain:
		message[:,k-1] = cipher[:,i]
		i += 1


	# turn message array to printable string
	plaintext = message.tobytes().decode('utf-8')
	plaintext = plaintext.replace(_filler_char, '')

	return plaintext
