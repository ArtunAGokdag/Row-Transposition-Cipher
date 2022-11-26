import numpy as np
from random import shuffle
from math import ceil
import encrypt as e
import decrypt as d


get_key_length = (lambda n: 2**(ceil(n/10)) if n < 100 else ceil(n/10))

def keygen(length):
	# Populate array with 1 to length
	choices = np.arange(1,length+1)

	shuffle(choices)
	
	# Turn array to string
	key = ''
	for k in choices:
		key += str(k)

	return key

def main():

	message = "Lorem ipsum dolor sit amet, Phasellus ullamcorper erat nibh, in dignissim felis eleifend vel. In sit amet massa quis dui.  "
	len_key = get_key_length(len(message))
	key = keygen(len_key)
	print(key)

	ciphertext = e.encrypt(message, key)
	print(ciphertext)

	message = d.decrypt(ciphertext, key)
	print(message)



if __name__ == '__main__':
	main()
