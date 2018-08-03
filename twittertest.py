import tweepy, csv

CONSUMER_KEY = "2iZwoiqZCyCeckD6RONU7yl79"
ACCESS_TOKEN = ""
CONSUMER_SECRET = ""
ACCESS_SECRET = ""

with open("consumersecret.key") as f:
    CONSUMER_SECRET = f.read().strip()
f.close()

with open("accesskey.key") as f:
    ACCESS_TOKEN = f.readline().strip()
    ACCESS_SECRET = f.readline().strip()
f.close()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


def displayUserInformation(username):
    user = api.get_user(username)
    userdict = user.__dict__['_json']
    for key in userdict:
        print(key + " : ", end="")
        print(userdict[key])

def displayUserTimeline(username, count=25, simple=False):
    for tweet in tweepy.Cursor(api.user_timeline, count=count, id=username).items():
        tweetdict = tweet.__dict__['_json']
        if simple:
            print("TweetID " + tweetdict['id_str'])
            print(tweetdict['text'])
            print("Date " + tweetdict['created_at'], end="\n\n")
        else:
            for key in tweetdict:
                print(key + " : ", end="")
                print(tweetdict[key])
        keys = tweet.__dict__.keys()
        print(keys)

def get_userinfo(name):
    user = api.get_user(name)
    user_info = [name.encode('utf-8'), user.name.encode('utf-8'), user.description.encode('utf-8'), user.followers_count, user.friends_count, user.created_at,	user.location.encode('utf-8')]
    print(user_info)

#displayUserTimeline('johnny_oliveira', count=10, simple=True)
#get_userinfo("PredaDante")
displayUserInformation("PredaDante")
