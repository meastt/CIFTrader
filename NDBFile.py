from flask import Flask, session,request,redirect
from google.cloud import ndb



class Basic(ndb.Model):
  email = ndb.StringProperty()
  first = ndb.StringProperty()
  last = ndb.StringProperty()
  middle = ndb.StringProperty()
  password = ndb.StringProperty()
  phone = ndb.StringProperty()
  