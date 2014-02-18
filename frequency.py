import os
import sys
import json

data = [] # define a list to contain all Twitter info

for line in open(sys.argv[1]):
    try:
    	data.append(json.loads(line.encode('utf-8'))) # Adding each line of the tweet file into the data list.
    except:
    	pass
    
def loadTweetList():
	allTweets = [] # define a list to contain all words in the Tweets
	for i in range(len(data)):
		if 'text' in data[i].keys(): # look for text key in data list item
			for word in data[i]['text'].split(): # split Tweet into words, add words into the list
				allTweets.append(word.strip().lower()) # clean, lowercase entries into allTweets list
	return allTweets

def wordCounter(wordList):
	for i in list(wordList): # cycle through the unique words in the tweet list
		tweetCounter = 0 # initialize counter
		for j in wordList: # cycle through all of the words in the tweet list
			if j.strip().lower() == i: # compare lowercase, clean word to unique value
				tweetCounter += 1
			else:
				tweetCounter += 0
		#print i.lower() + ":", float(tweetCounter/len(wordList))
		print i, float(tweetCounter)/len(wordList) # divide float counter by total values in list
		
wordCounter(loadTweetList())

#loadTweetList()