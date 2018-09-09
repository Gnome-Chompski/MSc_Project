import json, itertools

#Iterate through Google+ users and write the profiles marked as people objects
#to a new file as the original json files
def filter_pages():
    with open("usersGooglePlus.json", "r", encoding="utf-8") as file:
        with open("trueUsersGogglePlus.json", "a", encoding="utf-8") as userfile:
            counter = 0
            for line in file:
                dict = json.loads(line)
                type = dict["objectType"]

                if type == "person":
                    userfile.write(json.dumps(dict) + "\n")
                else:
                    counter += 1
    return counter

#Pair Google+ and Twitter ScreenNames into one file
def pair_ids():
    GIDs = {}
    #Add all google user ids to list
    with open("trueUsersGogglePlus.json", "r", encoding="utf-8") as file:
        for line in file:
            dict = json.loads(line)
            GIDs[dict['id']] = ""

    #Generate Twitter screenNames for the true IDs
    with open("datasetUserIdentification/google_plus_and_twitter_profiles.json", "r", encoding="utf-8") as userfile:
        for line in userfile:
            dict = json.loads(line)
            Gid = dict['Gid']
            if Gid in GIDs:
                GIDs[Gid] = dict["T_ScreenName"]

    #Write dictionary to file
    with open("twitterGooglePairs.txt", "a", encoding="utf-8") as pairfile:
        pairfile.write("Twitter_ScreenName - Google+ ID\n")
        for key, val in GIDs.items():
            pairfile.write(f"{key} - {val}\n")

#Pair Google+ and Twitter IDs into one file
def combine_ids():
    GIDs = {}
    #Add all google user ids to list
    with open("trueUsersGogglePlus.json", "r", encoding="utf-8") as file:
        for line in file:
            dict = json.loads(line)
            GIDs[dict['id']] = ""

    #Generate Twitter screenNames for the true IDs
    with open("datasetUserIdentification/google_plus_and_twitter_profiles.json", "r", encoding="utf-8") as userfile:
        for line in userfile:
            dict = json.loads(line)
            Gid = dict['Gid']
            if Gid in GIDs:
                GIDs[Gid] = dict["Tid"]

    #Write dictionary to file
    with open("twitterGoogleIDPairs.txt", "a", encoding="utf-8") as pairfile:
        pairfile.write("GoogleID - TwitterID\n")
        for key, val in GIDs.items():
            pairfile.write(f"{key} - {val}\n")

#Returns a dictionary of Google+ IDs as keys and Twitter screen names the as corresponding value
def read_GID_TSC_pairs():
    dict = {}
    with open("twitterGooglePairs.txt", "r", encoding="utf-8") as pairfile:
        for line in itertools.islice(pairfile, 1, None):
            pair = line.split(" - ")
            dict[pair[0]] = pair[1].strip()
    return dict

#Returns a dictionary of Google+ IDs as keys and Twitter IDs as the corresponding value
def read_GID_TID_pairs():
    dict = {}
    with open("twitterGoogleIDPairs.txt", "r", encoding="utf-8") as pairfile:
        for line in itertools.islice(pairfile, 1, None):
            pair = line.split(" - ")
            dict[pair[0]] = pair[1].strip()
    return dict

#Read in pairs of GID and their corresponding Twitter screen names
#Iterate through retrieved Twitter users if their screen name is present in any pair
#write to new file, twitter users present in both google+ and twitter sets
def remove_from_csv():
    dict = read_GID_TSC_pairs()
    with open("usersTwitter.csv", "r", encoding="utf-8") as file:
        with open("usersTrueTwitter.csv", "a", encoding="utf-8") as ufile:
            for line in itertools.islice(file, 1, None):
                data = line.split(",")
                print(data)
                if data[3] in dict.values():
                    ufile.write(line)

#Iterate through the Google+ JSON responses and write the desired attributes to a csv file
def filter_google_data():
    attributes = ["occupation", "gender", "id", "displayName", "tagline", "placesLived", "circledByCount", "name"]

    with open("usersGoogle.csv", "w", encoding="utf-8") as userfile:
        userfile.write(",".join(attributes) + "\n")
        with open("trueUsersGogglePlus.json", "r", encoding="utf-8") as datafile:
            for line in datafile:
                data = json.loads(line)
                attList = []
                for att in attributes:
                    try:
                        attList.append(str(data[att]).replace("\"", "\'"))
                    except KeyError:
                        attList.append(None)
                #Enclose item in quotations and delimit with ","
                attList = ["\"" + str(i) + "\"" for i in attList]
                attList = [" ".join(i.split()) for i in attList]
                userfile.write(",".join(attList) + "\n")


#print("No of pages " + str(filter_pages()))
#filter_twitter_users()
#remove_from_csv()
#print("done")
filter_google_data()
