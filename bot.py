import tweepy

API_KEY = 'rGEnYcWtRYXnN8cfgeIJxc2L8'
API_SECRET_KEY = 'MuqG2ax7wKanUeh88qMDkzrhcYx6h72Z5PfEioZiHCz12WsiEM'
ACCESS_TOKEN = '1392480361750228993-EjdtMXzlwCQXVmd1kshWV3MhFhmqTP'
ACCESS_TOKEN_SECRET = '70I86QvBryRGww5dg2oC5qWawOK2HmJIRfHyTEbrjHvLh'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

FILE = "id.txt"

def retrieve_id(file):
    f_read = open(file, "r")
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_id(id, file):
    f_write = open(file, "w")
    f_write.write(str(id))
    f_write.close()
    return

last_Seen_id = retrieve_id(FILE)
mentions = api.mentions_timeline(last_Seen_id, tweet_mode="extended")


for mention in reversed(mentions):
    if "100DaysOfCode" in mention.full_text:
        last_Seen_id = mention.id
        store_id(last_Seen_id, FILE)
        print("Reading Function")
        api.update_status('@'+mention.user.screen_name+'Keep up the good work')
        print('Replied to @'+mention.user.screen_name)
    else:
        print("Did not reply") 
