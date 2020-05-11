import webapp2
from webapp2_extras import jinja2

from model.like import Like
from model.tuit import Tuit
from utilities import Utilities


class ListTuitsHandler(webapp2.RequestHandler):
    def get(self):
        usr, url_usr, userActual = Utilities.checkUser()
        if userActual is None:
            return self.redirect("/")

        tuits = Tuit.query().order(-Tuit.dateTime)

        values = {
            "usr": usr,
            "url_usr": url_usr,
            "userActual": userActual,
            "tuits": tuits,
            "Like" : Like,
            "title": "Inicio"
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("home.html", **values))


app = webapp2.WSGIApplication([
    ('/tuits/list', ListTuitsHandler)
], debug=True)
