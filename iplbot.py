import tweepy
import iplapi as ip
import apikey

auth = tweepy.OAuthHandler(apikey.API_KEY, apikey.API_SECRET_KEY)
auth.set_access_token(apikey.ACCESS_TOKEN, apikey.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    
def tweeting(actual_tweet):
    api.update_status(actual_tweet)
    print("Succesfully tweeted")
ip.work()
        
tweeting("haiiii")