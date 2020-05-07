# Post published by a user

from google.appengine.ext import ndb

from user import User


class Tuit(ndb.Model):
    dateTime = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    text = ndb.StringProperty(required=True)
    user = ndb.KeyProperty(kind=User)

    @staticmethod
    def getTuit(req):
        try:
            id = req.GET["id"]
        except:
            id = ""

        return ndb.Key(urlsafe=id).get()
