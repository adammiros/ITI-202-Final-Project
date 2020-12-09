import tweepy
from tweepy.models import Status, User
import re
#Twitter API Setup
consumer_key = 'htDal3HAPxhPS5Z0hKodF66YV'
consumer_key_secret = 'N9LLBtXhEUuIu5xytkanW2W22BG4otS4n6NVv2hToWSF8Rayu1'

access_token = '589981127-k9nODgl00K59GKzWbASE5pTk03hHsuB3h817kE8G'
access_token_secret = 'Sqto4hjaf2EzpBmoqshx8Mm3kQ0jSNxOxGKBdjAu56CXW'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#######################

def getFityLatestTweets(userToLookup: str):

    ###Opening the tweets.txt file we will write to
    file = open("tweets.txt", mode="w", encoding="utf-8")

    #Checking if a username was entered
    if(userToLookup == "" or  userToLookup == " "):
        print("Since you did not provide a person to look up, we will use Joe Biden")
        userToLookup = "JoeBiden"
        for tweet in api.user_timeline(screen_name=userToLookup, tweet_mode='extended', count=50):
                tweet = re.sub(r"http\S+", "", tweet.full_text)
                file.writelines(tweet)
    else:
            for tweet in api.user_timeline(screen_name=userToLookup, tweet_mode='extended', count=50):
                    tweet = re.sub(r"http\S+", "", tweet.full_text)
                    file.writelines(tweet)



