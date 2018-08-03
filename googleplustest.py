import os, json
import google.oauth2.credentials
from pprint import pprint

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = "client_id_gplus.json"
SCOPES = ["https://www.googleapis.com/auth/userinfo.profile"]
API_SERVICE_NAME = "plus"
API_VERSION = "v1"

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(host='localhost',
        port=8080,
        authorization_prompt_message='Please visit URL: {url}',
        success_message='Auth flow is complete; close window',
        open_browser=True)
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def process_person(request_id, response, exception):
    if exception is not None:
        print("Exception Thrown")
    else:
        with open("usersGooglePlus.json", "a", encoding="utf-8") as file:
            file.write(json.dumps(response) + "\n")

service = get_authenticated_service()
# batch = service.new_batch_http_request()
# batch.add(service.people().get(userId="me"), callback=process_person)
# batch.add(service.people().get(userId="114985760485068752923"), callback=process_person)
# batch.execute(http=None)
people_resource = service.people()
people_document = people_resource.get(userId="106524158424097775579").execute()

pprint(people_document)
