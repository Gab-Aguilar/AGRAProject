# Rules
print('Guess one letter at a time. If you want to buy a vowel, you must have at least Php 500.00, otherwise, you cannot buy a vowel. If you think you know the word or phrase, type \'guess\' to guess the word or phrase. You will earn each letter at a set amount and vowels will not cost anything.')

from math import ceil
from random import randint
amounts = [500.00, 750.00, 1000.00, 1250.00, 1500.00, 1750.00, 5000.00]
total = 0

# List of letters to remove after each guess
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']
# Categories and words
categories = {'MOVIES': ['ENDGAME', 'PARASITE','THE DARK KNIGHT','TOY STORY','MAD MAX'], 'FRUITS':["GRAPES", "APPLE", "ORANGE", "BANANA","STRAWBERRY"], 'COUNTRIES':["ITALY", "JAPAN", "AFGHANISTAN", "PHILIPPINES","PERU"]}
# Pick a random category
category = randint(0, (len(categories) - 1))
# Print category name
print('Category:', list(categories.keys())[category])
# Get a random word or phrase from the category
word = (categories[list(categories.keys())[category]][randint(0, (len(list(categories[list(categories.keys())[category]])) - 1))]).upper()

#word = input().upper()
# Fill up list with blanks for characters in word
Word = []
for char in word:
	if char.isalpha():
		Word.append('_')
	else:
		Word.append(char)

# Function to print Word
def printWord(word):
	for char in word:
		print(char, end = ' ')
	print()
printWord(Word)

# List of all vowels
vowels = ['A', 'E', 'I', 'O', 'U']

# Keep guessing until word is guessed correctly
while True:
	while True:
		# Pick an random amount from amounts
		amount = amounts[randint(0,(len(amounts) - 1))]
		print('Php' + str(amount), 'per correct letter')
		print('Php 500.00 per vowel')
		guess = input().upper()
		# If the user wants to guess phrase or word
		if guess == 'GUESS':
			while True:
				correct = 0
				guess = input().upper()
				for letter in range(len(guess)):
					if guess[letter] == word[letter]:
						correct += 1
					else:
						break
				if correct == len(guess):
					for letter in range(len(guess)):
						if guess[letter] == word[letter]:
							if not Word[letter].isalpha():
								Word[letter] = guess[letter]
								if guess[letter] not in vowels and guess[letter].isalpha():
									total += amount
				else:
					print('Sorry, that\'s not the answer! Keep guessing!')
					printWord(Word)
					break
				if '_' not in Word:
					printWord(Word)
					print('You have: Php' + str(total))
					break
				else:
					for char in range(len(Word)):
						if word[char] == guess:
							Word[char] = guess
				print('Php' + str(total))
				printWord(Word)
				if '_' not in Word:
					break
			break
		# If user guesses letter they've already guessed
		elif guess not in alphabet:
			print('You\'ve already picked that letter!')
			print('You have: Php' + str(total))
		# If guess is a vowel, subtract $500 from total per vowel
		elif guess in vowels:
			if total >= 500:
				alphabet.remove(guess)
				for char in range(len(Word)):
					if word[char] == guess:
						total -= 500
						Word[char] = guess
			# If user cannot buy vowel
			else:
				print('Not enough money')
			print('You have: Php' + str(total))
			printWord(Word)
			if '_' not in Word:
				break
		# If everything else is False, remove letter from alphabet and replace char in Word with letter in word
		else:
			alphabet.remove(guess)
			for char in range(len(Word)):
				if word[char] == guess:
					Word[char] = guess
					total += amount
			print('You have: Php' + str(total))
			printWord(Word)
			if '_' not in Word:
				break
	# If word or phrase is fully guessed, end game
	if '_' not in Word:
		print('You won!')
		break