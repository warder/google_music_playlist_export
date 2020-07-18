
from gmusicapi import Mobileclient
import os.path

# https://play.google.com/music/listen#/pl/<playlist_token>
playlist_token = 'enter playlist token here'
# Authorized in google music mobile device ID
device_id = 'enter mobile device token here'
work_path = 'enter work path here'
playlist_file = f'{work_path}track_list.txt'
credential_file = f'{work_path}gm_cred_file'

if not os.path.exists(work_path):
    os.makedirs(work_path)

mobile_client = Mobileclient(debug_logging=True)
if not os.path.isfile(playlist_file):
    cred = Mobileclient.perform_oauth(storage_filepath=credential_file, open_browser=False)

mobile_client.oauth_login(device_id=device_id, oauth_credentials=credential_file)

is_authenticated = mobile_client.is_authenticated()
print(f'Auth :{is_authenticated}')

playlist_content = mobile_client.get_shared_playlist_contents(share_token=playlist_token)

track_list = ''
for i in playlist_content:
    artist = i["track"]["artist"]
    track_name = i["track"]["title"]
    track_list += f'{artist} - {track_name}\n'
print(track_list)

f = open(playlist_file, "w", encoding='utf-8')
print(f'Writing track list to file: {playlist_file}')
f.write(track_list)
f.close()
