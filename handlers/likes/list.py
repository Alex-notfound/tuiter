import webapp2
from webapp2_extras import jinja2

from model.tuit import Tuit
from model.like import Like
from utilities import Utilities


class ListLikesHandler(webapp2.RequestHandler):
    def get(self):
        usr, url_usr, userActual = Utilities.checkUser()
        if userActual is None:
            return self.redirect("/")
        tuit = Tuit.getTuit(self.request)
        likes = Like.getLikesByTuit(tuit.key)

        values = {
            "usr": usr,
            "url_usr": url_usr,
            "userActual": userActual,
            "tuit": tuit,
            "likes": likes,
            "Like": Like,
            "suggestedUsers": Utilities.suggestUsers(userActual),
            "title": "Likes"
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("list_likes.html", **values))


app = webapp2.WSGIApplication([
    ('/likes/list', ListLikesHandler)
], debug=True)
