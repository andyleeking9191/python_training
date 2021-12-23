# Hashtag Generator Challenge:
# Create a function that takes in the user input and outputs a string with a '#' at the begining.
# If there are multiple words given romove any spaceing between the words.

user_input = input("Enter text to be generated into a hashtag: ")

def hashtag_generator(text):
	hashtag_str = '#' + str(text).replace(' ', '')
	return hashtag_str

print(hashtag_generator(user_input))
