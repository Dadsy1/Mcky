from lineQR import *
from datetime import datetime
import asyncio, json, sys, time

############## Line QR ##############
cl = lineQR()
clset = cl.lineQr("IOSIPAD");;cl.apiJsonPrint(clset)
clpin = clset["Key"]
pp = cl.linePin(clpin);;cl.apiJsonPrint(pp)
cltk = cl.lineToken(clpin);;cl.apiJsonPrint(cltk)
token = cltk
print (f'Token Line : {str(token)}')

#----------------------------------------------------------------------------