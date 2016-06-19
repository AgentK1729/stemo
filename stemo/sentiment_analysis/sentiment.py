from successive import *
import threading

# Set initial value to 0; each thread adds its value to get final sentiment
global sentiment
sentiment = 0.0

# Create class for thread; each thread performs independent analysis
class sentimentThread (threading.Thread):
	def __init__ (self, tweets):
		threading.Thread.__init__(self)
		self.tweets = tweets

	def run (self):
		global sentiment
		for tweet in self.tweets:
			words = []
			# Get scores for each word
			words.append (getScores (tweet))
			# Get sentiment of each tweet
			sentiment += getSentiment (words)


def Sentiment (tweets):
	global sentiment
	threads = []
	# Split dataset into 5 parts
	temp = int(len(tweets)/5)

	# Initialize 5 threads to handle each part
	for i in range (5):
		threads.append (sentimentThread (tweets[(0+i*temp):(temp+i*temp)]))

	# Call run() method of thread
	for thread in threads:
		thread.start ()


	# Combine resuts of the threads
	for thread in threads:
		thread.join ()

	# Return the total value; combination of all threads
	return sentiment
