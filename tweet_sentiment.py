# This is a script that calculates the score of a given tweet using a predefined list of 
# words and their associated values. That list lives on my local so this script won't do much
# for you if you want to use it, but it does showcase some of the things I've done with Python.

import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    sent_file.seek(0)
    lines(tweet_file)
    tweet_file.seek(0)

# if __name__ == '__main__':
#    main()

afinnfile = open(sys.argv[1])

scores = {} # initialize an empty dictionary

for line in afinnfile:
    # The file is tab-delimited. "\t" means "tab character".
    term, score = line.split("\t")
    # Convert the score to an integer.
    scores[term] = int(score) 

# initialize an empty list
data = [] 

for line in open(sys.argv[2]):	
    # Adding each line of the tweet file into the data list.	
    data.append(json.loads(line.encode('utf-8'))) 

def findTweetScore():
    for i in range(len(data)):
    	tweetScore = 0
    	# look for text key in data list item
        if 'text' in data[i].keys(): 
            # set textString variable to tweet string in data list item, encode utf-8 to make it machine readable	
            textString = data[i]['text'].encode('utf-8')
            # call stringScore method with tweet string in data list item
            tweetScore = stringScore(textString) 
            # print tweet with score
            print float(tweetScore) 
        else:
            # print 0.0 because no tweet was found
            print float(tweetScore) 

def stringScore(tweetString):            
	totalWordScore = 0
	for word in tweetString.split():
		if word in scores:
			totalWordScore += scores[word]
		else:
			totalWordScore += 0
	return totalWordScore

findTweetScore()
