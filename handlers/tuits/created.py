
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.tuit import Tuit
from model.user import User


class CreatedTuitsHandler(webapp2.RequestHandler):
    def get(self):

        usr = users.get_current_user()

        if usr:
            url_usr = users.create_logout_url("/")
        else:
            url_usr = users.create_login_url("/")

        user = User.query(User.email == usr.email()).get()
        tuits = Tuit.query(Tuit.user == user.key).order(-Tuit.dateTime)

        values = {
            "usr": usr,
            "url_usr": url_usr,
            "tuits": tuits,
            "title": "Perfil de " + user.name
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **values))


app = webapp2.WSGIApplication([
    ('/tuits/created', CreatedTuitsHandler)
], debug=True)
