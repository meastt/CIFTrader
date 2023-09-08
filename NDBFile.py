from flask import Flask, session,request,redirect
from google.cloud import ndb



class Basic(ndb.Model):
  email = ndb.StringProperty()
  first = ndb.StringProperty()
  last = ndb.StringProperty()
  middle = ndb.StringProperty()
  password = ndb.StringProperty()
  phone = ndb.StringProperty()
  
class Items(ndb.Model):
    UpDate = ndb.DateTimeProperty(auto_now_add=True)
    MemberID = ndb.StringProperty()
    NSN = ndb.StringProperty()
    Price = ndb.StringProperty()
    Image = ndb.StringProperty()
    Available = ndb.BooleanProperty()
    SellorBuy = ndb.StringProperty()
        
