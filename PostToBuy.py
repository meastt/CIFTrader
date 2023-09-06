from flask import Flask, session, request, redirect, app
from flask import Response as DaResponse
from webapp3 import *


html1 = """
<html>
<head></head>
<body>


"""
# closing stuff goes here
html2 = """
</body>
</html>


"""


class BuyPage(BaseHandler):
    def get(self):
        self.response.write(html1)
        self.response.write("<h1>New Listing</h1>")
        self.response.write("""
        <form method="post" action="/buypage">
        NSN<input type="number" name="NSN" required><br>
        Item<input type="text" name="Item" required><br>
        <input  type="submit" value="Post your item">
        </form>

        """)

        self.response.write(html2)


def post(self):
    NSN = self.request.get("NSN")
    Item = self.request.get("Item")

    self.response.write(html1)
    self.response.write("<h1>New Listing</h1>")
    self.response.write("""
        Your item has been listed

        """)

    self.response.write(html2)
