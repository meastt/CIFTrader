from urllib.request import BaseHandler
from google.cloud import ndb

html1 = """
<html>
<head>
</head>
<body>
</body>
</html>
"""

html2 = """
<html>
<head>
</head>
<body>
</body>
</html>
"""

class Country(ndb.Model):
    United_States = ndb.StringProperty()
    NATO = ndb.StringProperty()
    West_Germany = ndb.StringProperty()
    Germany = ndb.StringProperty()
    Belgium = ndb.StringProperty()
    France = ndb.StringProperty()
    Italy = ndb.StringProperty()
    Czechoslovakia = ndb.StringProperty()
    Czech_Republic = ndb.StringProperty()
    Netherlands = ndb.StringProperty()
    South_Africa = ndb.StringProperty()
    Brazil = ndb.StringProperty()
    Canada = ndb.StringProperty()
    Denmark = ndb.StringProperty()
    Greece = ndb.StringProperty()
    Iceland = ndb.StringProperty()
    Norway = ndb.StringProperty()
    Portugal = ndb.StringProperty()
    Turkey = ndb.StringProperty()
    Luxembourg = ndb.StringProperty()
    Argentina = ndb.StringProperty()
    Japan = ndb.StringProperty()
    Isreal = ndb.StringProperty()
    Singapore = ndb.StringProperty()
    Spain = ndb.StringProperty()
    Malaysia = ndb.StringProperty()
    Thailand = ndb.StringProperty()
    Egypt = ndb.StringProperty()
    Republic_of_Korea = ndb.StringProperty()
    Estonia = ndb.StringProperty()
    Romania = ndb.StringProperty()
    Slovakia = ndb.StringProperty()
    Austria = ndb.StringProperty()
    Slovenia = ndb.StringProperty()
    Poland = ndb.StringProperty()
    United_Nations = ndb.StringProperty()
    Indonesia = ndb.StringProperty()
    Phillippines = ndb.StringProperty()
    Lithuania = ndb.StringProperty()
    Fiji = ndb.StringProperty()
    Tonga = ndb.StringProperty()
    Bulgaria = ndb.StringProperty()
    Hungry = ndb.StringProperty()
    Chile = ndb.StringProperty()
    Croatia = ndb.StringProperty()
    Republic_of_North_Macedonia = ndb.StringProperty()
    Latvia = ndb.StringProperty()
    Oman = ndb.StringProperty()
    Finland = ndb.StringProperty()
    Albainia = ndb.StringProperty()
    Kuwait = ndb.StringProperty()
    Ukraine = ndb.StringProperty()
    Belarus = ndb.StringProperty()
    Morocco = ndb.StringProperty()
    Sweden = ndb.StringProperty()
    Papa_New_Guinea = ndb.StringProperty()
    Australia = ndb.StringProperty()
    Georgia = ndb.StringProperty()
    Saudi_Arabia = ndb.StringProperty()
    United_Arab_Emirates = ndb.StringProperty()
    India = ndb.StringProperty()
    Serbia = ndb.StringProperty()
    Pakistan = ndb.StringProperty()
    Bosnia_Herzegoviana = ndb.StringProperty()
    Brunei_Darussalam = ndb.StringProperty()
    Montenegro = ndb.StringProperty()
    Jordan = ndb.StringProperty()
    Peru = ndb.StringProperty()
    Colombia = ndb.StringProperty()
    Qatar = ndb.StringProperty()
    Algeria =ndb.StringProperty()
    New_Zealand = ndb.StringProperty()
    United_Kingdom = ndb.StringProperty()

NumberDirect = {'00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26',
                '27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','52','53',
                '54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81',
                '82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99'}
    
def Assign(NumberDirect):
    User = input("Enter the NCB number: ")
    if User in NumberDirect:
        if User == '00':
            return Country.United_States
        elif User == "01":
            return Country.United_States
        elif User == "02":
            return Country.United_States
        elif User == "03":
            return Country.United_States
        elif User == "04":
            return Country.United_States
        elif User == "05":
            return Country.United_States
        elif User == "06":
            return Country.United_States
        elif User == "07":
            return Country.United_States
        elif User == "08":
            return Country.United_States
        elif User == "09":
            return Country.United_States
        elif User == "10":
            return Country.United_States
        elif User == "11":
            return Country.NATO
        elif User == "12":
            return Country.West_Germany
        elif User == "13":
            return Country.Belgium
        elif User == "14":
            return Country.France
        elif User == "15":
            return Country.Italy
        elif User == "16":
            return Country.Czechoslovakia
        elif User == "17":
            return Country.Netherlands
        elif User == "18":
            return Country.South_Africa
        elif User == "19":
            return Country.Brazil
        elif User == "20":
            return Country.Canada
        elif User == "21":
            return Country.Canada
        elif User == "22":
            return Country.Denmark
        elif User == "23":
            return Country.Greece
        elif User == "24":
            return Country.Iceland
        elif User == "25":
            return Country.Norway
        elif User == "26":
            return Country.Portugal
        elif User == "27":
            return Country.Turkey
        elif User == "28":
            return Country.Luxembourg
        elif User == "29":
            return Country.Argentina
        elif User == "30":
            return Country.Japan
        elif User == "31":
            return Country.Isreal
        elif User == "32":
            return Country.Singapore
        elif User == "33":
            return Country.Spain
        elif User == "34":
            return Country.Malaysia
        elif User == "35":
            return Country.Thailand
        elif User == "36":
            return Country.Egypt
        elif User == "37":
            return Country.Republic_of_Korea
        elif User == "38":
            return Country.Estonia
        elif User == "39":
            return Country.Romania
        elif User == "40":
            return Country.Slovakia
        elif User == "41":
            return Country.Austria
        elif User == "42":
            return Country.Slovenia
        elif User == "43":
            return Country.Poland
        elif User == "44":
            return Country.United_Nations
        elif User == "45":
            return Country.Indonesia
        elif User == "46":
            return Country.Phillippines
        elif User == "47":
            return Country.Lithuania
        elif User == "48":
            return Country.Fiji
        elif User == "49":
            return Country.Tonga
        elif User == "50":
            return Country.Bulgaria
        elif User == "51":
            return Country.Hungry
        elif User == "52":
            return Country.Chile
        elif User == "53":
            return Country.Croatia
        elif User == "54":
            return Country.Republic_of_North_Macedonia
        elif User == "55":
            return Country.Latvia
        elif User == "56":
            return Country.Oman
        elif User == "58":
            return Country.Finland
        elif User == "59":
            return Country.Albainia
        elif User == "60":
            return Country.Kuwait
        elif User == "61":
            return Country.Ukraine
        elif User == "62":
            return Country.Belarus
        elif User == "63":
            return Country.Morocco
        elif User == "64":
            return Country.Sweden
        elif User == "65":
            return Country.Papa_New_Guinea
        elif User == "66":
            return Country.Australia
        elif User == "68":
            return Country.Georgia
        elif User == "70":
            return Country.Saudi_Arabia
        elif User == "71":
            return Country.United_Arab_Emirates
        elif User == "72":
            return Country.India
        elif User == "73":
            return Country.Serbia
        elif User == "74":
            return Country.Pakistan
        elif User == "75":
            return Country.Bosnia_Herzegoviana
        elif User == "76":
            return Country.Brunei_Darussalam
        elif User == "77":
            return Country.Montenegro
        elif User == "78":
            return Country.Jordan
        elif User == "79":
            return Country.Peru
        elif User == "80":
            return Country.Colombia
        elif User == "81":
            return Country.Qatar
        elif User == "82":
            return Country.Algeria    
        elif User == "98":
            return Country.New_Zealand
        elif User == "99":
            return Country.United_Kingdom
        else: 
            return "Country not found"
    else:
        return "Invaid Number"


    

    








SuppplyClass={}



class NSNnumber(BaseHandler):
    def get(self):
        self.response.write(html1)
        self.response.write("""
        <form method = "POST" type = "text" action = "/NSNnumber">
        <input type = "text" name = "FSCG"><input type = "text" name = "ncb"><input type = "text" name = "niin">
        <input type = "submit">
        </form>
                             
        """)
        self.response.write(html2)
    def post(self):
        client = ndb.Client()
        with client.context():
            self.response.write(html1)
            FSCG = self.request.get("FSCG")
            NCB = self.request.get("NCB")
            NIIN = self.request.get("niin")
            dabasic = Basic()
            dabasic.FSCG = FSCG
            dabasic.NCB = NCB
            dabasic.NIIN = NIIN
            dabasic.put()
            self.response.write("""
            your information is recorded 
            """)
            self.response.write(html2)

class FSCG(BaseHandler):
    def get(self):
        self.response.write(html1)
        self.resoponse.write("""
        <form method = "POST" type = "text" action = "/NSNnumber">
        <input type = "text" name = "FSCG"><input type = "text" name = "ncb"><input type = "text" name = "niin">
        <input type = "submit">
        </form>
        """) 
        self.response.write(html2)
    def post(self):
        client = ndb.Client()
        with client.context():
            self.response.write(html1)
            FSCG = self.request.get("FSCG")
            NCB = self.request.get("NCB")
            NIIN = self.request.get("niin")
            dabasic = Basic()
            dabasic.FSCG = FSCG
            dabasic.NCB = NCB
            dabasic.NIIN = NIIN
            dabasic.put()
            self.response.write("""
            your information is recorded 
            """)
            self.response.write(html2)

class NCB(BaseHandler):
    def get(self):
        client = ndb.Client()
        with client.context():
            NcbNum = Country()
            ncb.NcbNum = ""
            

        self.response.write("""
        """)
        self.response.write(html2)
class NIIN(BaseHandler):
    def get(self):
        self.response.write(html1)
        self.response.write("""
        """)
        self.response.write(html2)