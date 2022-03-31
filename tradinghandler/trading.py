from requests import post, get, put
import pandas as pd

class TradingInteractor():
    def __init__(self, accountname, url = "192.168.178.36"):
        self.url = "http://%s:30002/" % url
        self.accountname = accountname
        self.portfolio = self.getPortfolio()

    def getPortfolio(self):
        url = self.url + "portfolio/" + self.accountname
        self.portfolio = get(url).json()
        return self.portfolio

    def getUSD(self):
        self.getPortfolio()
        return self.portfolio["USDT"]

    def getData(self, symbol, lookback = 1):
        # lookback is in days
        url = self.url + "priceHistoric/" + symbol + "/" + str(lookback)
        data = get(url).json()
        data = pd.DataFrame(data)
        # it is reversed, so switch around
        data = data.iloc[::-1]
        return data

    def getApeWisdomSymbol(self, symbol, lookback):
        url = self.url + "apewisdom/" + symbol + "/" + str(lookback)
        return get(url).json()

    def getApeWisdomLast(self):
        url = self.url + "apewisdom/"
        return get(url).json()

    def buy(self, symbol, amountInUSD):
        url = self.url + "buy/" + self.accountname + "/" + symbol + "/" + str(amountInUSD) + "?amountInUSD=true"
        self.portfolio = put(url).json()
        return self.portfolio

    def sell(self, symbol, amountInUSD = -1):
        url = self.url + "sell/" + self.accountname + "/" + symbol + "/" + str(amountInUSD) + "?amountInUSD=true"
        self.portfolio = put(url).json()
        return self.portfolio