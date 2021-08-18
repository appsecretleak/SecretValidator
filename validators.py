import json

import requests


def is_valid_twitter_credential(key, secret):
    API_END_POINT = "https://api.twitter.com/oauth2/token"
    r = requests.post(API_END_POINT, data={"grant_type": "client_credentials"}, auth=(key, secret))
    # print(r.text)
    if r.status_code == 200 and "access_token" in r.text:
        return True
    else:
        return False


def is_valid_facebook_credential(key,secret):
    API_END_POINT = "https://graph.facebook.com/oauth/access_token?redirect_uri=&grant_type=client_credentials&client_id={id}&client_secret={secret}"
    url = API_END_POINT.format(id=key, secret=secret)
    r = requests.get(url)
    # print(r.text)
    if r.status_code == 200:
        return True
    else:
        return False

def is_valid_youTube_credential(key):
    url = "https://www.googleapis.com/youtube/v3/activities?part=contentDetails&maxResults=25&channelId=UC-lHJZR3Gqxm24_Vd_AJ5Yw&key=" + key
    r = requests.get(url)
    # print(r.text)
    if r.status_code == 200:
        return True
    else:
        return False


def is_valid_google_translation_credential(key):
    url = "https://translation.googleapis.com/language/translate/v2?key=" + key
    headers = {"Content-Type": "application/json"}
    data = {"q": "brother in law","target": "zh"}
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    # print(r.text)
    if r.status_code == 200:
        return True
    else:
        return False


def is_valid_google_cloud_vision_credential(key):
    url = "https://vision.googleapis.com/v1/images:annotate?key=" + key
    headers = {"Content-Type": "application/json"}
    data = {"requests":[{"image":{"source":{"imageUri":"https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"}},"features":[{"type":"LOGO_DETECTION","maxResults":1}]}]}
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    # print(r.text)
    if r.status_code == 200:
        return True
    else:
        return False

# For Google Maps Validator, you may refer to https://github.com/ozguralp/gmapsapiscanner
