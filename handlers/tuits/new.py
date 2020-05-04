# coding: utf-8
# New tuit

import webapp2
import time
from webapp2_extras import jinja2

from model.tuit import Tuit


class NewTuitHandler(webapp2.RequestHandler):
    def get(self):

        values = {
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("new_tuit.html", **values))

    def post(self):
        text = self.request.get("textTuit", "")

        tamText = len(text)
        if tamText < 1 or tamText > 280:
            return self.redirect("/")
        else:
            tuit = Tuit(text=text)
            tuit.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/tuits/new', NewTuitHandler)
], debug=True)
