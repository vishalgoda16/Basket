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
    
    basket = Basket()

    basket.addProduct('Component',3,'bag','walmart',223,'EUR')

    basket.getBalance('Component')

    basket.addProduct('collection',5,'toys','walmart',122,'EUR')

    basket.addProduct('bundle',3,'package','walmart',22,'EUR')

    basket.getProductList()

    basket.getBalance('Component')

    basket.addProduct('Component',6,'bat','walmart',22,'EUR')

    basket.getBalance('Component')

    basket.getProductList()

    basket.addProduct('Component',6,'sss','walmart',2,'EUR')

    basket.getProductList()

    basket.value()

    getExchangeRate()

    # https://github.com/vishalgoda16/Basket.git --> Repo link