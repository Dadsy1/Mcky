import asyncio,json
from .sunucu import *
from .ayarlar import *



class lineAPI(Ayarlar,Sunucu):
    
    def __init__(self):
        Ayarlar.__init__(self)
        Sunucu.__init__(self)

    @staticmethod
    def apiPrint(opps):
        print(opps)
        
    @staticmethod
    def apiJsonPrint(textp: dict):
        print(json.dumps(textp,indent=4,ensure_ascii=False))
        
    def lineQr(self,codetk):
        return asyncio.run(self.sets9s(self.LINE_QR_HOST,self.LINE_QR_ENDPOINT + f"/{codetk}",key9e="json"))
        
    def linePin(self,ids):
        return asyncio.run(self.sets9s(self.LINE_QR_HOST,self.LINE_P_ENDPOINT + f"/{ids}",key9e="json"))
    
    def lineToken(self,ids):
        return asyncio.run(self.sets9s(self.LINE_QR_HOST,self.LINE_T_ENDPOINT + f"/{ids}",key9e="json"))
    
    def lineLiff(self,token,appname,url):
        self.sett["url"]= url
        self.sett["token"] = token
        self.sett["appname"]= appname
        self.sets["Content-Type"] = 'application/json'
        return asyncio.run(
            self.sets9s(
                self.LINE_LIFF_HOST,
                self.LINE_LIFF_ENDPOINT,
                key9e="text",
                sets=self.sets,
                sett=self.sett
            ))
