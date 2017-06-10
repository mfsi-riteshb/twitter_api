import tweepy
import sys
from tweepy.error import TweepError
import  ipdb

# global api variable
api = None

def configure():
    consumer_key = "< your Consumer key >" 
    consumer_secret = "< Your consumer secret >"
    access_token = "< your access token >"
    access_token_secret= "< your access token secret >"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # setting global variable api to use it globally.
    global api
    api = tweepy.API(auth)

def get_user(user_name):
    try:
        return api.get_user(user_name)
    except TweepError as tw:
        print "User Not Found"

def get_tweets(user):
    if hasattr(user, 'timeline'):
        tweets = user.timeline()
        for tweet in tweets:
            print tweet.text

def main(argv):
    configure()
    get_tweets(
	get_user(argv[0])
    )

if __name__ == "__main__":
   main(sys.argv[1:])
