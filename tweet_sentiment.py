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
    term, score = line.split("\t") # The file is tab-delimited. "\t" means "tab character".
    scores[term] = int(score) # Convert the score to an integer.

# print scores.items() # Print every (term, score) pair in the dictionary.

# initialize an empty list
data = [] 

for line in open(sys.argv[2]):	
    data.append(json.loads(line.encode('utf-8'))) # Adding each line of the tweet file into the data list.

def findTweetScore():
    for i in range(len(data)):
    	tweetScore = 0
        if 'text' in data[i].keys(): # look for text key in data list item
            textString = data[i]['text'].encode('utf-8') # set textString variable to tweet string in data list item, encode utf-8 to make it machine readable
            tweetScore = stringScore(textString) # call stringScore method with tweet string in data list item
            print float(tweetScore) # print tweet with score
        else:
        	print float(tweetScore) # print 0.0 because no tweet was found

def stringScore(tweetString):            
	totalWordScore = 0
	for word in tweetString.split():
		if word in scores:
			totalWordScore += scores[word]
		else:
			totalWordScore += 0
	return totalWordScore

findTweetScore()
