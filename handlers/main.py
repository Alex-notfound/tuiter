# coding: utf-8
# !/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from datetime import datetime

import webapp2

from webapp2_extras import jinja2
from utilities import Utilities


class MainHandler(webapp2.RequestHandler):
    def get(self):
        usr, url_usr, userActual = Utilities.checkUser()
        jinja = jinja2.get_jinja2(app=self.app)

        if userActual is None:
            values = {
                "usr": usr,
                "url_usr": url_usr,
                "title": "Registrate"
            }
            self.response.write(jinja.render_template("index.html", **values))
        else:
            return self.redirect("/tuits/list")

    def post(self):
        name = self.request.get("name", "")
        birthDate = self.request.get("nacimiento", "")

        tamName = len(name)

        try:
            fechaNac = datetime.strptime(birthDate, "%Y-%m-%d").date()
            if tamName < 1 or tamName > 50 or fechaNac >= datetime.now().date():
                return self.redirect("/")
            Utilities.logUser(name, fechaNac)
        except:
            print("Datos invalidos")
            return self.redirect("/")

        return self.redirect("/tuits/list")


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
