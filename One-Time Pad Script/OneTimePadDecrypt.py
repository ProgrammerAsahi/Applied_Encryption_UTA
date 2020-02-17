def one_time_pad_decrypt():
	# Open the file to read key and messages
	f = open("OTPInputCT.txt", "r")
	# Read key
	key = f.readline()
	# Read encrypted message
	encrypted_message = f.readline()
	f.close()
	#Display the encrypted message on console
	print("The encrypted message is:\n" + encrypted_message + "\n")
	# Set the alphabet
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	# Split the key into a list
	key = (key.split())[:-1]
	# Initialize our result as empty string
	decrypted_message = ""
	# This j index is used to record which key number should be used next in the key list
	j = 0
	# Iterate the encrypted message
	for i in range(len(encrypted_message)):
		letter = encrypted_message[i]
		# If current character is a letter
		if letter in alphabet:
			# Turn the encryted letter into index for calculation
			offset = ord(letter) - ord('A') if letter.isupper() else ord(letter) - ord('a')
			# Use the key to decryt the encryted index and get the original index 
			original_offset = offset - int(key[j])
			# Make sure the original index is between 0 and 25
			original_offset %= 26
			# Turn the original index into letter again and remain the same upper or lower cases as those in the encrypted message
			original_letter = chr(ord('A') + original_offset) if letter.isupper() else chr(ord('a') + original_offset)
			# Add our decrypted letter to the tail of the result string
			decrypted_message += original_letter
			# One key number is used, j plus 1
			j += 1
		else: # If current character is not a letter
			decrypted_message += letter # Just add this character to the tail of the result string
			# Also, no key number is used in this case, j will remain the same
	# Output the result
	print("The decrypted message is:\n" + decrypted_message)


one_time_pad_decrypt()