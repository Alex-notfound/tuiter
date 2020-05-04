# User that uses the app

from google.appengine.ext import ndb


class User(ndb.Model):

    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)