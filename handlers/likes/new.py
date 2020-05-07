# coding: utf-8
# New like

import webapp2
import time
from model.like import Like
from model.tuit import Tuit
from utilities import Utilities


class NewLikeHandler(webapp2.RequestHandler):

    def get(self):

        usr, url_usr, userActual = Utilities.checkUser()

        try:
            if usr:
                tuit = Tuit.getTuit(self.request)
                if not Like.exists(userActual.key, tuit.key):
                    like = Like(tuit=tuit.key, user=userActual.key)
                    like.put()
                    time.sleep(2)
        finally:
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/likes/new', NewLikeHandler)
], debug=True)
