import sys

def word_picker(difficulty):
	try:
		dictionary = open("wordlist.txt", "r")
	except IOError:
		print "Failed to open file!"
		sys.exit(1)
	

difficulty = raw_input("Choose difficulty (1 - Easy, 2 - Medium, 3 - Hard)\n> ")
word = word_picker(difficulty)

