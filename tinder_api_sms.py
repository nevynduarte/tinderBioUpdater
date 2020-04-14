# coding=utf-8
import json
import datetime
import requests
import os

headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    "content-type": "application/json",
    "User-agent": "Tinder/7.5.3 (iPhone; iOS 10.3.2; Scale/2.00)",
	"X-Auth-Token": os.environ['TINDER_TOKEN'],
}

def update_profile(bio):
    '''
    ex: update_profile(bio="bio")
    kwargs: a dictionary - whose keys become separate keyword arguments and the values become values of these arguments
    bio: "bio"
    '''
    try:
        url = host + '/profile'
        r = requests.post(url, headers=headers, data=json.dumps({"bio": "This is the time"}))
        return r.json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong. Could not change your profile:", e)

if __name__ == '__main__':
    host = 'https://api.gotinder.com'
    #leave tinder_token empty if you don't use phone verification
    tinder_token = os.environ['TINDER_TOKEN']
    print(update_profile("bio"))
