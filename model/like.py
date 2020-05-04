# Like is given to a post from a user

from google.appengine.ext import ndb

from tuit import Tuit
from user import User


class Like(ndb.Model):
    dateTime = ndb.DateTimeProperty(auto_now_add=True)
    tuit = ndb.KeyProperty(kind=Tuit)
    user = ndb.KeyProperty(kind=User)
