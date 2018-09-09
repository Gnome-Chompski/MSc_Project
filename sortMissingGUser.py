import os, json, itertools
import google.oauth2.credentials
from pprint import pprint

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

"""
Very similar to the extraction script for G+ users the aim here is to find out
issues with quota limits and API calls. So additional variables are used to
keep track of errors.
"""

CLIENT_SECRETS_FILE = "client_id_gplus.json"
SCOPES = ["https://www.googleapis.com/auth/userinfo.profile"]
API_SERVICE_NAME = "plus"
API_VERSION = "v1"

#Read lines in file from START to END
START = 0
END = 244

#Track number of errors, total, 404 and 403
MISTAKES = 0
m404 = 0
m403 = 0

#Return the service object
def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(host='localhost',
        port=8080,
        authorization_prompt_message='Please visit URL: {url}',
        success_message='Auth flow is complete; close window',
        open_browser=True)
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

#Batch request callback, handle a single response
def process_person(request_id, response, exception):
    global MISTAKES
    global m404
    global m403
    if exception is not None:
        exc = str(exception)
        if "HttpError 404" in exc:
            print(request_id + " not found")
            m404 += 1
        elif "HttpError 403" in exc:
            with open("missedGUsers3.txt", "a", encoding="utf-8") as mfile:
                mfile.write(request_id.strip() + "\n")
                m403 += 1
        else:
            print("A different kind of error " + type(exception))
        MISTAKES += 1
    else:
        with open("usersGooglePlus.json", "a", encoding="utf-8") as file:
            file.write(json.dumps(response) + "\n")

service = get_authenticated_service() #API object
batch = service.new_batch_http_request() #Batch object

with open("missedGUsers3.txt", "r", encoding="utf-8") as userFile:
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
print("404 errors = " + str(m404))
print("403 errors = " + str(m403))
print("Duplicate IDs number is " + str(counter))
