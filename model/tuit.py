# Post published by a user

from google.appengine.ext import ndb


class Tuit(ndb.Model):

    dateTime = ndb.DateTimeProperty(auto_now_add=True)
    text = ndb.StringProperty(required=True)
