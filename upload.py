import progressbar
import httplib2

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

# https://developers.google.com/api-client-library/python/guide/aaa_client_secrets


def get_authenticated_service():
    flow = flow_from_clientsecrets(
        "client_secrets.json", scope="https://www.googleapis.com/auth/youtube", message="no")

    storage = Storage("oauth.json")
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage)

    return build("youtube", "v3", http=credentials.authorize(httplib2.Http()))


def upload_done(request_id, response, exception):
    try:
        print("Added", response["snippet"]["resourceId"]["channelId"], "({})".format(response["snippet"]["title"]))
    except:
        print(exception)

youtube = get_authenticated_service()
batch = youtube.new_batch_http_request(callback=upload_done)

print("Generating request...")
with open("channels.txt") as channels:
    for channel in channels:
        batch.add(youtube.subscriptions().insert(
          part='snippet',
          body=dict(
            snippet=dict(
              resourceId=dict(
                channelId=channel
              )
            )
        )))

print("Sending batch request")
batch.execute()
