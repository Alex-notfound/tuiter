# User that uses the app

from google.appengine.ext import ndb


class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    birthDate = ndb.DateProperty()
    email = ndb.StringProperty(required=True)

    @staticmethod
    def getUserByEmail(email):
        return User.query(User.email == email).get()

    @staticmethod
    def getUser(req):
        try:
            id = req.GET["id"]
        except:
            id = ""

        return ndb.Key(urlsafe=id).get()
