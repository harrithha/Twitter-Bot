from bs4 import BeautifulSoup
import tweepy
import apikey
import iplapi as ip
import time

auth = tweepy.OAuthHandler(apikey.API_KEY, apikey.API_SECRET_KEY)
auth.set_access_token(apikey.ACCESS_TOKEN, apikey.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
start = 0
pre = 0
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

while(1):
    try:
        print("Await Score")
        api.update_status(ip.live_scores())
        time.sleep(300)
    except:
        print("Wait")
        continue


    
    


    


