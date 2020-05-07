import time

from webapp2_extras.users import users

from model.user import User


class Utilities:

    def __init__(self):
        pass

    @staticmethod
    def checkUser():

        usr = users.get_current_user()

        if usr:
            url_usr = users.create_logout_url("/")
            if not User.getUserByEmail(usr.email()):
                user = User(name=usr.nickname(), email=usr.email())
                user.put()
                time.sleep(2)
            user = User.getUserByEmail(usr.email())
        else:
            url_usr = users.create_login_url("/")
            user = User(name="invitado")

        return usr, url_usr, user
