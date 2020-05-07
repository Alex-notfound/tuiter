# coding: utf-8
# New tuit

import webapp2
import time

from google.appengine.ext import ndb
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.tuit import Tuit
from model.user import User
from utilities import Utilities


class NewTuitHandler(webapp2.RequestHandler):
    def get(self):
        usr, url_usr, userActual = Utilities.checkUser()

        values = {
            "usr": usr,
            "url_usr": url_usr,
            "userActual": userActual,
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("new_tuit.html", **values))

    def post(self):
        text = self.request.get("textTuit", "")
        tamText = len(text)
        if tamText < 1 or tamText > 280:
            return self.redirect("/")

        usr = users.get_current_user()
        user = User.getUserByEmail(usr.email())
        tuit = Tuit(text=text, user=user.key)
        tuit.put()
        time.sleep(2)
        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/tuits/new', NewTuitHandler)
], debug=True)
