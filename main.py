import numpy as np
from random import shuffle
import encrypt as e
import decrypt as d

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

	message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus ullamcorper erat nibh, in dignissim felis eleifend vel. In sit amet massa quis dui.  "
	key = keygen(11)
	print(key)

	ciphertext = e.encrypt(message, key)
	print(ciphertext)

	message = d.decrypt(ciphertext, key)
	print(message)



if __name__ == '__main__':
	main()
