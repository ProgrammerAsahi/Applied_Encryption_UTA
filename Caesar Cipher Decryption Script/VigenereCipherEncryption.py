
def vigenere_encrypt(message, key):
	
	#Capitalize the letters in message and key
	message = message.upper()
	key = key.upper()
	
	vigenere_table = dict()
	
	#Initialize the alphabet
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	#Create vigenere table
	#There are 2 layers of loops because vigenere table is 2-dimensioned
	for index_letter1 in range(0, 26):
		for index_letter2 in range(0, 26):
			if index_letter2 == 0:
				vigenere_table[alphabet[index_letter1]] = dict()
			#Map the specific encryted letter with the specific original 2 letters
			vigenere_table[alphabet[index_letter1]][alphabet[index_letter2]] = alphabet[(index_letter1 + index_letter2) % 26]

	
	newMessage = ""
	#Iterate each char in the message and encrypt every letter by looking up the vigenere table
	for i in range(len(message)):
		if message[i] in alphabet: #If the char is a letter
			newMessage += vigenere_table[message[i]][key[i % len(key)]]
		else: #If the char is not a letter
			newMessage += message[i] 

	#Display the encrypted result
	print("The Decrypted message is: " + newMessage)

#Notify the user to input key and message
key = input("Please input an alphabetic string as key:\n")
message = input("Please input the message you want to encrypt:\n")

#Call the encryption function
vigenere_encrypt(message, key)