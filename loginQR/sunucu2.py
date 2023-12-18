import aiohttp




class Sunucu(object):
    
    def __init__(self):
        self.sapi = {}
        self.napi = {}
        
        
    async def setss(self,qapi,capi,texts, sapi=None,napi=None):
        
        setapi = aiohttp.ClientSession()
        async with setapi as zapi:
            rapis = qapi+capi
            async with zapi.get(rapis,headers=sapi, json=napi) as fapi:
                if texts == "text":
                    return await fapi.text()
                elif texts == "json":
                    return await fapi.json(content_type='application/json')