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



file = open("tweets.txt", mode="w", encoding="utf-8")

#######################

def getFityLatestTweets(userToLookup: str):
    if(userToLookup == "" or  userToLookup == " "):
        print("Since you did not provide a person to look up, we will use Joe Biden")
        userToLookup = "JoeBiden"
        for tweet in api.user_timeline(screen_name=userToLookup, tweet_mode='extended', count=50):
            if ('RT @' not in tweet.full_text):
                tweet = re.sub(r"http\S+", "", tweet.full_text)
                print("Tweet: " + tweet + "\n")

                print("Writting to tweet.txt...")
                file.writelines(tweet)
    else:
        print("Looking up latest tweets for: " + userToLookup)
        for tweet in api.user_timeline(screen_name=userToLookup, tweet_mode='extended', count=50):
            if ('RT @' not in tweet.full_text):
                tweet = re.sub(r"http\S+", "", tweet.full_text)
                print(tweet.full_text + "\n")
                print("Tweet: " + tweet + "\n")

                print("Writting to tweet.txt...")
                file.writelines(tweet)


    file.close()
