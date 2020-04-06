import requests 
import json

base = 'https://financialmodelingprep.com/api/v3/'
ticker = 'MGM'
quarter = 'quarter'
response = requests.request('GET', base + 'financials/cash-flow-statement/{}?period={}'.format(ticker, quarter))

jsonBody = response.json()
print (json.dumps(jsonBody))

def create_app():
    for i in range(10):
        print ("Hello")