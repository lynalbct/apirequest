from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ACCESS_TOKEN = "885776662532456448-bqF2tH7LZdQCQsNg8fWWE3DC3JEqD7U"
ACCESS_TOKEN_SECRET = "MixbCzZvAwDSFu5na4VMiICNkHktanvIzY8pQMFlyIUGv"
CONSUMER_KEY = "G9l0afgnfLAKt7ju9hQ2aEJZ3"
CONSUMER_SECRET = "k5ey0rxjAwgByQa10EY4m7GDRKjtIkYz18wop8KfCNIRaW1mJA"

class listener(StreamListener):
	def on_data(self,data):
		print data
		return True
	def on_error(sef,status):
			print status

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["A tweet"])