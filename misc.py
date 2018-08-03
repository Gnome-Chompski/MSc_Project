import tweepy, csv, numpy, json
import pandas as pd
from pprint import pprint

with open("handlesTwitter.txt", "r", encoding="utf-8") as users:
    for line in users:
        FILENAME = "userTweets/" + line.strip() + ".csv"
        print("Processing " + line.strip())
        with open(FILENAME, "r", encoding="utf-8") as file:
            data = file.readlines()

        line1 = data[0].partition("retweeted")
        corrected = [line1[0] + line1[1] + "\n", line1[2]]
        corrected.extend(data[1:])

        with open(FILENAME, "w", encoding="utf-8") as file:
            file.writelines(corrected)
