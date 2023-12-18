import asyncio,json
from .sunucu import *
from .ayarlar import *



class lineQR(Ayarlar,Sunucu):
    
    def __init__(self):
        Ayarlar.__init__(self)
        Sunucu.__init__(self)

    @staticmethod
    def apiPrint(opps):
        print(opps)
        
    @staticmethod
    def apiJsonPrint(textp: dict):
        print(json.dumps(textp,indent=4,ensure_ascii=False))
        
    def lineQr(self,tokenqr):
        return asyncio.run(self.setss(self.LINE_QR_HOST,self.LINE_QR_ENDPOINT + f"/{tokenqr}",tests="json"))
        
    def linePin(self,ids):
        return asyncio.run(self.setss(self.LINE_QR_HOST,self.LINE_P_ENDPOINT + f"/{tests}",tests="json"))
    
    def lineToken(self,ids):
        return asyncio.run(self.setss(self.LINE_QR_HOST,self.LINE_T_ENDPOINT + f"/{tests}",tests="json"))
    
    def lineLiff(self,token,appname,url):
        self.sett["url"]= url
        self.sett["token"] = token
        self.sett["appname"]= appname
        self.sets["Content-Type"] = 'application/json'
        return asyncio.run(
            self.setss(
                self.LINE_LIFF_HOST,
                self.LINE_LIFF_ENDPOINT,
                texts="text",
                sets=self.sets,
                sett=self.sett
            ))