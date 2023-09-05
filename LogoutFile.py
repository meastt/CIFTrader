from datetime import date, datetime
from webapp3 import *
from NDBFile import ndb
import email
import ReaseachDa

class Basic(ndb.model):
    username = ndb.StringProperty()
    password = ndb.StringProperty()
    email = ndb.StringProperty()
    first = ndb.StringProperty()
    last = ndb.StringProperty()
    phone = ndb.StringProperty()



html1 = """
<html>
<head>
</head>
<body>
</body>
</html>
"""

html2 = """
html>
<head>
</head>
<body>
</body>
</html>
"""


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

class Update(BaseHandler):
    def get(self): 
        client = ndb.Client()
        with client.context():
            self.response.write(html1)
            self.response.write("""
            <form method = "POST" action = "/update">
            username:<input type = "text" name = "username">
            password:<input type = "text" name = "password">
            email:<input type = "text" name = "email">
            first:<input type = "text" name = "first">
            last:<input type = "text" name = "last">
            phone:<input type = "text" name = "phone">
            <input type = "submit" value = "update">
            </form>
            """)
            self.response.write(html2)
            self.response.write(html2)
    def post(self):
        client = ndb.Client()
        with client.context():
            self.response.write(html1)
            email = self.request.get("email")
            first = self.request.get("first")
            basicsearch = ndb.gql("SELECT * FROM Basic where email =: email and first =: first", email = email, first = first)
            for a in basicsearch:
                dakey = a.key.get()
                dakey.email = email()
                dakey.first = first()
                dakey.put()
            self.response.write("""
your information has been updated
""")
            self.response.write(html2)

class NewAccount(BaseHandler):
    def get(self):
        client = ndb.Client()
        with client.context():
            self.response.write(html1)
            self.response.write("""
            <form method = "POST" action = "/NewAccount">
            username:<input type = "text" name = "username"> 
            password:<input type = "text" name = "password">
            email:<input type = "text" name = "email">
            first:<input type = "text" name = "first"> 
            last:<input type = "text" name = "last">
            phone:<input type = "text" name = "phone">
            <input type = "submit"> 
            </form>
""")
    def post(self):
        client = ndb.Client()
        with client.context():
            self.response.write(html1)
            username = self.request.get("username") 
            password = self.request.get("password")
            email = self.request.get("email")
            first = self.request.get("first")
            last = self.request.get("last")
            phone = self.request.get("phone")
            dabasic = Basic()
            dabasic.username = username
            dabasic.password = password
            dabasic.email = email
            dabasic.first = first
            dabasic.last = last 
            dabasic.phone = phone
            dabasic.put()
            self.response.write("""
your information has been updated
""")
            self.response.write(html2)
            