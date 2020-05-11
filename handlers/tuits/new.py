# coding: utf-8
# New tuit

import webapp2
import time

from webapp2_extras import jinja2

from model.tuit import Tuit
from utilities import Utilities


class NewTuitHandler(webapp2.RequestHandler):
    def get(self):
        usr, url_usr, userActual = Utilities.checkUser()
        if userActual is None:
            return self.redirect("/")

        values = {
            "usr": usr,
            "url_usr": url_usr,
            "userActual": userActual,
            "suggestedUsers": Utilities.suggestUsers(userActual),
            "title": "Tuitear"
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("new_tuit.html", **values))

    def post(self):
        usr, url_usr, userActual = Utilities.checkUser()
        if userActual is None:
            return self.redirect("/")

        text = self.request.get("textTuit", "")
        tamText = len(text)
        if tamText < 1 or tamText > 280:
            return self.redirect("/tuits/list")

        tuit = Tuit(text=text, user=userActual.key)
        tuit.put()
        time.sleep(2)
        return self.redirect("/tuits/list")


app = webapp2.WSGIApplication([
    ('/tuits/new', NewTuitHandler)
], debug=True)
