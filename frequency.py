# This is a simple script created for a Coursera data science project to count the frequency of unique words
# in an entire list of tweets. It's not much, but it's something I did.

import os
import sys
import json

# define a list to contain all Twitter info
data = [] 

for line in open(sys.argv[1]):
    try:
    	# Adding each line of the tweet file into the data list.
    	data.append(json.loads(line.encode('utf-8'))) 
    except:
    	pass
    
def loadTweetList():
	# define a list to contain all words in the Tweets
	allTweets = [] 
	for i in range(len(data)):
		# look for text key in data list item
		if 'text' in data[i].keys(): 
			# split Tweet into words, add words into the list
			for word in data[i]['text'].split(): 
				# clean, lowercase entries into allTweets list
				allTweets.append(word.strip().lower()) 
	return allTweets

def wordCounter(wordList):
	# cycle through the unique words in the tweet list
	for i in list(wordList): 
		# initialize counter
		tweetCounter = 0 
		# cycle through all of the words in the tweet list
		for j in wordList: 
			# compare lowercase, clean word to unique value
			if j.strip().lower() == i: 
				tweetCounter += 1
			else:
				tweetCounter += 0
		# divide float counter by total values in list		
		print i, float(tweetCounter)/len(wordList) 
		
wordCounter(loadTweetList())

#loadTweetList()
