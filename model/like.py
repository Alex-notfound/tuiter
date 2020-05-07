# Like is given to a post from a user

from google.appengine.ext import ndb

from tuit import Tuit
from user import User


class Like(ndb.Model):
    dateTime = ndb.DateTimeProperty(auto_now_add=True)
    tuit = ndb.KeyProperty(kind=Tuit)
    user = ndb.KeyProperty(kind=User)

    @staticmethod
    def getLikesByTuit(tuit):
        return Like.query(Like.tuit == tuit).order(-Like.dateTime)

    @staticmethod
    def exists(user, tuit):
        return Like.query(Like.tuit == tuit, Like.user == user).get()
