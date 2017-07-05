import re
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from textblob import TextBlob
from tweepy import Stream
import json
from pprint import pprint
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


#Variables that contains the user credentials to access Twitter API 
access_token = "828392731139506176-fIkWgydz0fzrmWSo6kWMoxLqVQZxVRu"
access_token_secret = "A7LUXVVAFWTEVh67NZNjrMqBrrVR8FbuNgiwbWjAHQBPi"
consumer_key = "i7HAB7tsd68VCQUR2hGl3vz6J"
consumer_secret = "nvVcLE1Trpt0007kvirrBlujjca3D6ZLYZtSFj6d4j0aAuwmtQ"

class StdOutListener(StreamListener):

	def on_data(self, data):
        
		data_full = str(data) + '\n'
		#print (data)
		json_data = json.loads(data)
		pprint(json_data['text'])
		
		json_data['text'] = json_data['text'].encode('utf-8').decode('ascii','ignore')
		sentiment = []

		analyzer = SentimentIntensityAnalyzer()
		sentiment = analyzer.polarity_scores(json_data['text'])				
		tweetWrite = str(json_data['created_at']).split(' ')[1]+str(json_data['created_at']).split(' ')[2]+' '+str(sentiment['compound'])
				
		with open('fetched_tweets.txt','a') as tf:
			tf.write(tweetWrite + '\n')
		return True

    
	def on_error(self, status):
			print (status)


	def clean_tweet(self, tweet):
		
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
		

	def get_tweet_sentiment(self, tweet):
		
		
		analysis = TextBlob(self.clean_tweet(tweet))
	
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'


def main():
	
	l = StdOutListener()
	
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
	stream.filter(track=['ibm'])



if __name__ == "__main__":

	main()
