from flask import Flask, session,request,redirect, app
from flask import Response as DaResponse
from webapp3 import *
from LogoutFile import *
from ReaseachDa import *




app = Flask(__name__)


class MainPage(BaseHandler):
    def get(self):
        f = open("static/index.html", "r")
        daindex=str(f.read())
        self.response.write(daindex)

class Test(BaseHandler):
    def get(self):
        f = open("static/index.html", "r")
        daindex=str(f.read())
        self.response.write(daindex)



app.secret_key = 'djfkadsjiwisjj3344'

@app.route('/',methods=['GET','POST'])    
def MainDef():
    return webapp(MainPage())



@app.route('/<searchURL>',methods=['GET','POST'])    
def RouteDef(searchURL):    
    app = webapp2.WSGIApplication([
    ("/test", Test),
    ("/Login", Login)
    ]
    , searchURL=searchURL ) 
    return webapp(app()) 




