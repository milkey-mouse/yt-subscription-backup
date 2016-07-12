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


def add_subscription(youtube, channel_id):
    return

youtube = get_authenticated_service()

with open("channels.txt", "w") as channels:
    subscriptions = youtube.subscriptions()
    request = subscriptions.list(part='snippet', mine=True)
    while request is not None:
        result = request.execute()
        for channel in result["items"]:
            channels.write(channel["snippet"]["resourceId"]["channelId"])
            channels.write("\n")
            try:
                print(channel["snippet"]["resourceId"]["channelId"],
                      "({})".format(channel["snippet"]["title"]))
            except UnicodeEncodeError:  # for stupid terminals that dont do Unicode
                print(channel["snippet"]["resourceId"]["channelId"])
        request = subscriptions.list_next(request, result)
