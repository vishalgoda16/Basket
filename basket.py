import requests
import json

def getExchangeRate(sym):
    results=requests.get('https://api.exchangeratesapi.io/latest?base=%'%sym)
    print(json.loads(results.content)['rates']['CAD'])

class Basket:
    def __init__(self):
        self.__product={}
        
    def addProduct(self,sym,qty,name,seller,price,currency):
        if qty<0:
            raise ValueError()
        self.__product[sym]= {
            "quantity":self.getBalance(sym)+qty,
            "description": name,
            "seller":seller,
            "price":price,
            "currency": currency
        }
            
    def removeProduct(self,sym,qty):
        if qty<0 or qty>self.__product[sym]:
            raise ValueError()
        self.__product[sym]=self.getBalance(sym)-qty
        
    def getBalance(self,sym):
        if sym not in self.__product:
            return 0
        return self.__product[sym]['quantity']
    
    def getProductList(self):
        return self.__product
    
    def value(self):
        total=0
        for k,i in self.__product.items():
            total += int(i['quantity'])*int(i['price'])*getExchangeRate()
        return total