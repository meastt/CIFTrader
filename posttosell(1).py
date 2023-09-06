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
        NSN=self.request.get("NSN")
        Price=self.request.get("Price")
        imagefile=self.request.POST.get("imagefile")
        self.response.write(html1)
        self.response.write("<h1>New Listing</h1>")
        self.response.write("""
        Your item has been listed
        

        """)

        self.response.write(html2)