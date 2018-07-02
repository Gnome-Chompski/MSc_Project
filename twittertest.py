import tweepy

CONSUMER_KEY = "92TERgNQ6JPXybIvaocgVQvhG"
ACCESS_TOKEN = ""
CONSUMER_SECRET = ""
ACCESS_SECRET = ""

with open("consumersecret.key") as f:
    CONSUMER_SECRET = f.read().strip()

with open("accesskey.key") as f:
    ACCESS_TOKEN = f.readline().strip()
    ACCESS_SECRET = f.readline().strip()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def displayUserInformation(username):
    user = api.get_user(username)
    userdict = user.__dict__['_json']
    for key in userdict:
        print(key + " : ", end="")
        print(userdict[key])

def displayUserTimeline(username, count=25, simple=False):
    timeline = api.user_timeline(username, count = count)
    for tweet in timeline:
        tweetdict = tweet.__dict__['_json']
        if simple:
            print("TweetID " + tweetdict['id_str'])
            print(tweetdict['text'])
            print("Date " + tweetdict['created_at'], end="\n\n")
        else:
            for key in tweetdict:
                print(key + " : ", end="")
                print(tweetdict[key])


def get_userinfo(name):
    user = api.get_user(name)
    user_info = [name.encode('utf-8'), user.name.encode('utf-8'), user.description.encode('utf-8'), user.followers_count, user.friends_count, user.created_at,	user.location.encode('utf-8')]
    print(user_info)

#displayUserTimeline('PredaDante', simple=True)
get_userinfo("PredaDante")
displayUserInformation("VisitScotland")
