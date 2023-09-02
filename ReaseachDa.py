from flask import Flask, session,request,redirect,app
from flask import Response as DaResponse
from webapp3 import *
from NDBFile import *
from datetime import date, datetime
from mock import *

class LogininPro(BaseHandler):
    def daLoginout(self):
        client = ndb.Client()
        with client.context():
            signedin = self.session.get("signedin")
        if signedin==True:
            daReturn += """
            <li><a href = "/login">My Account</a></li>
    """
        else:
            daReturn = """<li>< href="/login">Log In</a></li>
    """
        return daReturn

    def Denied(Signedin):
        client = ndb.Client()
        with client.context():
            signedin = self.session.get("signedin")
        if signedin==False:
            daReturn += """
            denied
"""
