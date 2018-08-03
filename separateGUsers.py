import json, itertools

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

def filter_twitter_users():
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

def read_dict_pairs():
    dict = {}
    with open("twitterGooglePairs.txt", "r", encoding="utf-8") as pairfile:
        for line in itertools.islice(pairfile, 1, None):
            pair = line.split(" - ")
            dict[pair[0]] = pair[1].strip()
    return dict

def remove_from_csv():
    dict = read_dict_pairs()
    with open("usersTwitter.csv", "r", encoding="utf-8") as file:
        with open("usersTrueTwitter.csv", "a", encoding="utf-8") as ufile:
            for line in itertools.islice(file, 1, None):
                data = line.split(",")
                print(data)
                if data[3] in dict.values():
                    ufile.write(line)

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
                attList = ["\"" + str(i) + "\"" for i in attList]
                attList = [" ".join(i.split()) for i in attList]
                userfile.write(",".join(attList) + "\n")


#print("No of pages " + str(filter_pages()))
#filter_twitter_users()
#remove_from_csv()
#print("done")
filter_google_data()
