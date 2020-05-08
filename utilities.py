import time
import datetime

from webapp2_extras.users import users

from model.user import User


class Utilities:

    def __init__(self):
        pass

    @staticmethod
    def checkUser():

        usr = users.get_current_user()
        user = User.getUserByEmail(usr.email())
        print(user)
        if user is None:
            url_usr = users.create_login_url("/")
        else:
            url_usr = users.create_logout_url("/")

        return usr, url_usr, user

    @staticmethod
    def logUser(name, birthDate):

        usr = users.get_current_user()

        if usr:
            url_usr = users.create_logout_url("/")
            user = User(name=name, email=usr.email(),
                        birthDate=datetime.datetime.strptime(birthDate, "%Y-%m-%d").date())
            user.put()
            time.sleep(2)
        else:
            url_usr = users.create_login_url("/")
            user = User(name="invitado")

        return usr, url_usr, user
