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
                ,password
                ,expiration=60):

        self.user       = user
        self.password   = password
        self.expiration = expiration

        self.referer = 'https://www.arcgis.com'

        self.creds = {"username": self.user
                     ,"password":self.password
                     ,"f": "json"
                     ,"referer": self.referer
                     ,"expiration":self.expiration}

    def gettoken(self):

        response = requests.post('{0}/sharing/generateToken'.format(self.referer)
                                ,data=self.creds)

        jsonresponse = json.loads(response.text)

        if 'error' in jsonresponse:
            raise ValueError("got response {0} from generateToken".format(jsonresponse))
        
        # full good response like 
        # {'token': 'abcdiluvesri247',
        #  'expires': 1672338298003,
        #  'ssl': True}
        token = jsonresponse['token']

        # print(token)

        return token

class Layer(object):

    def __init__(self):

        pass