import requests
import json

def getExchangeRate(sym):
    results=requests.get('https://api.exchangeratesapi.io/latest?base=%'%sym)
    print(json.loads(results.content)['rates']['CAD'])