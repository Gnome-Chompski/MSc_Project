import os, json, itertools
import google.oauth2.credentials
from pprint import pprint

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = "client_id_gplus.json"
SCOPES = ["https://www.googleapis.com/auth/userinfo.profile"]
API_SERVICE_NAME = "plus"
API_VERSION = "v1"

#Start Reading from line in file
START = 10000
#Stop reading from line in file
END = 10571

MISTAKES = 0

#Return API object to make requests to Google+ API
def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(host='localhost',
        port=8080,
        authorization_prompt_message='Please visit URL: {url}',
        success_message='Auth flow is complete; close window',
        open_browser=True)
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

#Callback function, deals with each person request
def process_person(request_id, response, exception):
    global MISTAKES
    if exception is not None:
        with open("missedGUsers.txt", "a", encoding="utf-8") as mfile:
            mfile.write(request_id.strip() + "\n")
            MISTAKES += 1
    else:
        with open("usersGooglePlus.json", "a", encoding="utf-8") as file:
            file.write(json.dumps(response) + "\n")

#Create service and Http batch objects
service = get_authenticated_service()
batch = service.new_batch_http_request()

#Iterate through segments of the list to add to the batch request
with open("handlesGoogle.txt", "r", encoding="utf-8") as userFile:
    counter = 0
    addedInBatch = 0
    for line in itertools.islice(userFile, START, END):
        try:
            batch.add(service.people().get(userId=line.strip()), callback=process_person, request_id=line.strip())
            addedInBatch += 1
        except KeyError:
            counter += 1
            continue
        #print(line)
batch.execute(http=None)

print("Profiles added to batch request " + str(addedInBatch))
print("Number of errors is " + str(MISTAKES))
print("Duplicate IDs number is " + str(counter))
