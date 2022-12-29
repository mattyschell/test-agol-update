# This is an arcgisonline management module
# with arcgisonline.user, arcgisonline.layer, etc classes 

# I have cribbed a lot of this from a script where
#__authors__ = ["Esri", "DVG"]
#__license__ = "GPLv3"

import requests
import json



class User(object):

    def __init__(self
                ,user 
                ,password):

        self.user = user
        self.password = password
        # this one is not https?
        # todo: try with https and then use referer in gettoken post
        self.referer = 'http://www.arcgis.com'

        self.creds = {"username": self.user
                     ,"password":self.password
                     ,"f": "json"
                     ,"referer": self.referer}

    def gettoken(self):

        response = requests.post("https://www.arcgis.com/sharing/generateToken"
                                ,data=self.creds)

        # full response like 
        # {'token': 'abcdiluvesri247',
        #  'expires': 1672338298003,
        #  'ssl': True}
        token = json.loads(response.text)['token']

        return token


class Layer(object):

    def __init__(self):

        pass