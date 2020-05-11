import time

from webapp2_extras.users import users

from model.like import Like
from model.user import User


class Utilities:

    def __init__(self):
        pass

    @staticmethod
    def checkUser():

        usr = users.get_current_user()
        user = User.getUserByEmail(usr.email())

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
                        birthDate=birthDate)
            user.put()
            time.sleep(2)
        else:
            url_usr = users.create_login_url("/")
            user = User(name="invitado")

        return usr, url_usr, user

    @staticmethod
    def suggestUsers(user):
        return User.query(User.key != user.key).fetch(limit=3);
