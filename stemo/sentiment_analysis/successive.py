# -*- coding: utf-8 -*-
from sqlite3 import connect, InterfaceError

# Word class to hold word and corresponding scores
class Word (object):
	def __init__ (self, word, scores):
		self.word = word
		# List of all scores based on connotation
		self.scores = scores

	# Routine for printing objects of Word class
	def __str__ (self):
		scores = ""
		for score in self.scores:
			scores += str (score) + " "
		return self.word + ": " + scores


# Returns all scores for a word
def getScores (word):  # Take a word and return a Word object
	newWord = Word (word, [])
	conn = connect ("wordlist.db")
	cur = conn.cursor ()

	# Query the database to get scores
	query = "select * from word where word = ?"
	try:
		cur.execute (query, (word,))
		for row in cur:
			# append to list of scores
			newWord.scores.append (row[1]-row[2])
	except InterfaceError:
		# If not found, assign token positive score; assigning 0.0 messes up the calculation
		newWord.scores.append (0.01)

	conn.close ()
	return newWord



# Successive deviation
def getSentiment (words):
	final_scores = []

	if len (words) == 1:
		return words[0].scores[0]

	else:
		# First two words
		Min = 1.0
		best = (0, 0)
		for i in words[0].scores:
			for j in words[1].scores:
				diff = abs (i-j)
				if diff < Min:
					best = (i, j)
					Min = diff

		final_scores.append (best[0])
		final_scores.append (best[1])

		# Rest of the words
		for i in words[2:]:
			score = final_scores[-1]
			Min = 1.0
			for j in i.scores:
				if abs (score-j) < Min:
					Min = j
			final_scores.append (Min)

		sentiment = 0
		for i in final_scores:
			sentiment += i
		return sentiment
