def NoSpecials(text):
	text = text.upper()
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	goodChars = alphabet + " \n\t\"?"

	#this step is not stricktly necessary
	#turn our message into a list of individual symbols
	message = list(text)
	NewMessage = []

	#run through the list of our message,, throwing out special characters
	for symbol in message:
		if symbol in goodChars:
			NewMessage.append(symbol)

	NewMessage = ''.join(NewMessage)
	return NewMessage

def load():
	dictionary = open("dictionary.txt", "r")
	#dictionary = open("Test_dictionary.txt", "r")
	#make the dictionary into a list
	WordList = (dictionary.read().split('\n'))[:-1] # the[:-1] cuts of the empty element

	dictionary.close()
	return WordList

def WordRatio(message):

	Dict = load()
	message = NoSpecials(message)

	words = message.split()

	counter = 0

	for word in words:
		if word in Dict:
			counter += 1
	
	ratio = counter/float(len(words))

	return ratio

def isEnglish(message):
	if WordRatio(message) >= 0.5:
		return True
	else:
		return False

def caesar_decrypt():
	#Read in our file
	message = open("CaesarInput.txt", "r")
	text = message.readline() #Read the decrypted message from the file to our variable
	message.close()

	#Create the Alphabet
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	#Capitalize the encryted text
	text = text.upper()

	print(text)
	#Initialize our target decrypted message as an empty string
	decryptMessage = ""

	#Iterate the key from 1 to 25 to find the right key and decrypt the message
	for key in range(1, 26):
		newMessage = ""
		#Use the key to decrypt each letter in the sentence
		for letter in text:
			if letter in alphabet:
				index = alphabet.index(letter) #Find the index of the current decrypted letter
				index = index - key #Recover to the index of the original letter
				index = index % 26 #Make sure the index is between 0 to 25
				letter = alphabet[index] #Get the original letter by using original index and looking up the alphabet
			newMessage += letter #Append the decrypted letter to the tail of our new message

		#If the decrypted message is normal English, this means we have found the right key
		if isEnglish(newMessage):
			decryptMessage = newMessage
			break #We have found the right key and the original text, the loop is useless now and we can jump out from the loop
	print(decryptMessage) #Print the original text to the console

caesar_decrypt() # call the function to decrypt the message encrypted by Caesar Cipher