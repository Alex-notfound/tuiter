import webapp2
from webapp2_extras import jinja2
from model.tuit import Tuit
from model.user import User
from utilities import Utilities


class CreatedTuitsHandler(webapp2.RequestHandler):
    def get(self):
        usr, url_usr, userActual = Utilities.checkUser()

        user = User.getUser(self.request)
        userActual = User.getUserByEmail(usr.email())
        tuits = Tuit.query(Tuit.user == user.key).order(-Tuit.dateTime)

        values = {
            "usr": usr,
            "url_usr": url_usr,
            "userActual": userActual,
            "tuits": tuits,
            "title": "Perfil de " + user.name
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **values))


app = webapp2.WSGIApplication([
    ('/tuits/created', CreatedTuitsHandler)
], debug=True)
