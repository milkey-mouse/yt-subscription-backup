# subscriber-backup
Back up a list of your YouTube subscribers to restore to at any time (even on another account)

This is a script I made in 5 minutes to migrate to a new Google account while keeping my subscriptions.

#How to use
- Create a `[client_secrets.json](https://developers.google.com/api-client-library/python/guide/aaa_client_secrets)` and put it in the root directory
- Install the Google Python API client: `pip install --upgrade google-api-python-client`
- Run `backup.py` (with Python 3)
- Copy `channels.txt` to all your favorite places

#How to restore
- Copy `channels.txt` back to the root directory
- If migrating to a new channel, delete `oauth.json`
- Run `upload.py`
