from SmartApi import SmartConnect, SmartWebSocket
import pandas as pd
import pyotp
import xlwings as xw
from logzero import logger
import requests
import json
import os
from datetime import datetime, timedelta
import sys
from credentials import *

sma = SmartConnect(api_key)
data = sma.generateSession(username,password,pyotp.TOTP(qr_key).now())
# print(data)

authToken = data['data']['jwtToken']
refreshToken =data['data']['refreshToken']

# fetch the feedtoken
feedToken = sma.getfeedToken()
# print(feedToken)
#fetch USER PROFILE
res = sma.getProfile(refreshToken)
sma.generateToken(refreshToken)



