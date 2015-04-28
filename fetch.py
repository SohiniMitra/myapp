from TwitterSearch import *
from textblob import TextBlob
def search(text,limit):
	tweets_list = []
	try:
	    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
	    tso.set_keywords(text) # let's define all words we would like to have a look for
	    tso.set_language('en') # we want to see English tweets only
	    tso.set_include_entities(False) # and don't give us all those entity information

	    # it's about time to create a TwitterSearch object with our secret tokens
	    ts = TwitterSearch(
		consumer_key = 	'tbHIo3PImh0pSIETLlO8wIKj4',
		consumer_secret = 'QmzJYSAp9rw6O7tDJATkm7Avq0OBRTfZbdNf3BjEmDmdDB1jT2',
		access_token = '1315897358-IkDrUD4Zdy6HP3FjF4UxdBqICEZOU91Lys95FGu',
		access_token_secret = 'nHROttog8743ZmeBWeldvh24EHwXtW4h1Z69o1GsgV2zE'
	     )

	     # this is where the fun actually starts :)
	    cnt=0
	    for tweet in ts.search_tweets_iterable(tso):
		cnt+=1
		if cnt>limit:
		    break
	        tweets_list.append(tweet['text'])
		#print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
	    print cnt,'tweets'

	except TwitterSearchException as e: # take care of all those ugly errors if there are some
	    print(e)
	return tweets_list

def sentiment_analysis(text,limit):
	tweets_list = search(text,limit) 
	sentiments = []
	pos=0
	neg=0
	pos_sum = 0.0
	neg_sum = 0.0	
	for tweet in tweets_list:
		tweet = ''.join([i if ord(i) < 128 else '' for i in tweet])
		blob = TextBlob(tweet)
		print tweet,blob.sentences[0].sentiment.polarity
		sent = blob.sentences[0].sentiment.polarity
		if sent>0:
			pos+=1
			pos_sum+=sent
		else:
			neg+=1
			neg_sum+=sent
	pos_sum/=pos
	neg_sum/=neg
	print pos_sum,neg_sum
	if pos_sum>=(-neg_sum):
		return True
	else:
		return False

print sentiment_analysis(['Avengers'],10)
