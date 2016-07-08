# Final Project, Brian Bowles, March 31, 2015.
import sys

scores = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, 
		  "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, 
		  "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, 
		  "Z": 10}

rack = raw_input('Please enter your scrabble rack (enter a space for a blank tile): ')
words = []
scrabble_words = {}
valid = False
total = 0
best = ""
all = ''

try:
	with open("ScrabbleWords.txt", "r") as f:
		for line in f:
			words.append(line.strip())
except EnvironmentError:
	print("Could not find file path.")
	exit(1)	

for word in words:
	rack_list = list(rack)
	for letter in word:
		for tile in rack_list:
			if tile == ' ':
				valid = True
				rack_list.remove(tile)
				break
			elif letter.upper() == tile.upper():
				valid = True
				rack_list.remove(letter.upper())
				total = total + scores[letter.upper()]
				break
			else:
				valid = False
	if valid == True:
		scrabble_words.update({word: total})
	total = 0

total = 0		
for word in scrabble_words:
	if total < scrabble_words[word]:
		total = scrabble_words[word]
		best = word
		
print("The best word is: " + best)
all = raw_input("List all possible words? (Y/N): ")

if (all.upper() == 'Y'):
	for word in scrabble_words:
		print word
		
print rack_list ##Debugging
