from datetime import date, datetime
from webapp3 import *
from NDBFile import ndb 

class Login(BaseHandler):
    def get(self):
        self.data = {}
        self.username = input("Username")
        self.password = input("password")
        client = ndb.Client()
        with client.context():
            self.response.write(LoginHtml.format(LogInOUT=daLogInOUT(self),page="Log In",))

class Logout(BaseHandler):
    def get(self):
        client = ndb.Client()
        with client.context():
            self.response.write(LoginHtml.format(page = "Log out", logout = """<a href='/login'>Log In<a>"""))
            self.session['signedin'] = False
            self.response.write("You are signed out")
            self.response.write(LogoputHml)
            