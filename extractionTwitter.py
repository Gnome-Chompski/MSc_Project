# import tweepy, csv, numpy
# import pandas as pd
# from pprint import pprint
#
# CONSUMER_KEY = "2iZwoiqZCyCeckD6RONU7yl79"
# ACCESS_TOKEN = ""
# CONSUMER_SECRET = ""
# ACCESS_SECRET = ""
#
# with open("consumersecret.key") as f:
#     CONSUMER_SECRET = f.read().strip()
# f.close()
#
# with open("accesskey.key") as f:
#     ACCESS_TOKEN = f.readline().strip()
#     ACCESS_SECRET = f.readline().strip()
# f.close()
#
# #Handle authentication and intialise the api object to make calls to
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#
#
# username = "PredaDante"
#
# userAttributes = []
# with open("userAttributes.csv", "r", encoding="utf-8") as fl:
#     userAtt = csv.reader(fl, delimiter=",")
#     for item in userAtt:
#         userAttributes.append(item)
# userAttributes[0].pop()
# userAttributes = userAttributes[0]
#
# tweetHeaders = []
# with open("tweetAttributes.csv", "r", encoding="utf-8") as tA:
#     tweetAtt = csv.reader(tA, delimiter=",")
#     for item in tweetAtt:
#         tweetHeaders.append(item)
# tweetHeaders[0].pop()
# tweetHeaders = tweetHeaders[0]
#
#
# with open("usersTwitter.csv", "w", encoding="utf-8") as userFile:
#     userFile.write(",".join(userAttributes) + "\n")
#     with open("handlesTwitter.txt", "r", encoding="utf-8") as  screenNameFile:
#         for name in screenNameFile:
#             username = name
#             tweets = "userTweets/" + username.strip() + ".csv"
#             with open(tweets, "w", encoding="utf-8") as tweetFile:
#                 tweetFile.write(",".join(tweetHeaders))
#                 try:
#                     for tweet in tweepy.Cursor(api.user_timeline, id=username, count=100).items():
#                         tweetdict = tweet.__dict__['_json']
#                         userDict = tweetdict['user']
#                         userID = tweetdict['user']['id_str']
#                         tweetdict['user'] = userID
#                         line = list(tweetdict.values())
#                         line = ["\"" + str(i) + "\"" for i in line]
#                         tweetFile.write(",".join(line) + "\n")
#                 except tweepy.TweepError:
#                     print(username + " not found or for some other reason inaccessible")
#                     continue
#             userlist = ["\"" + str(j) + "\"" for j in list(userDict.values())]
#             userFile.write(",".join(userlist) + "\n")
# userFile.close()
