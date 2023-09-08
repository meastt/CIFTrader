from flask import Flask, session,request,redirect, app
from flask import Response as DaResponse
from webapp3 import *


html1="""
<html>
<head></head>
<body>


"""
#closing stuff goes here
html2="""
</body>
</html>


"""
def FormUpload(ContentType,FileType,MemberID,DaFile):
    DocType=ContentType
    daTime= datetime.now()
    AtEnd=".png"
   
    filename = FileType + MemberID + str(daTime.date())+str(daTime.time())+AtEnd
    

    #daForm = FormData(MemberID= MemberID,filename=filename,FileType=FileType,ContentType=ContentType)     
    #daForm.put()
    client = storage.Client(project="CIFTrader")
    bucket = client.get_bucket("CIFTrader.appspot.com")
    blob = Blob(filename, bucket)
    blob.upload_from_file(DaFile)
    messtome='A form has been uploaded by '+MemberID
    

class SellPage(BaseHandler):
    def get(self):
        self.response.write(html1)
        self.response.write("<h1>New Listing</h1>")
        self.response.write("""
        <form method="post" action="/sellpage" enctype="multipart/form-data">
        NSN<input type="number" name="NSN" required><br>
        Price<input type="text" name="Price" required><br>
        Upload Image<input type="file" name="imagefile" required><br>
        <input  type="submit" value="Post your item">
        </form>

        """)

        self.response.write(html2)
    def post(self):
        client = ndb.Client()
        with client.context():
            NSN=self.request.get("NSN")
            Price=self.request.get("Price")
            imagefile=self.request.POST.get("imagefile")
            #FormUpload()
            self.response.write(html1)
            self.response.write("<h1>New Listing</h1>")
            self.response.write("""
            Your item has been listed
            

            """)

            self.response.write(html2)