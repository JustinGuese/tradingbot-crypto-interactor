from requests import post, get, put
import pandas as pd

class TradingInteractor():
    def __init__(self, accountname, url = "198.74.104.172"):
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

    def buy(self, symbol, amountInUSD):
        url = self.url + "buy/" + self.accountname + "/" + symbol + "/" + str(amountInUSD) + "?amountInUSD=true"
        resp = put(url)
        if resp.status_code == 200:
            self.portfolio = resp.json()["portfolio"]
            return self.portfolio
        else:
            raise ValueError("could not buy %s.errorcode: %s, errormessage: %s" % (symbol, str(resp.status_code), str(resp.text)))

    def sell(self, symbol, amountInUSD = -1):
        url = self.url + "sell/" + self.accountname + "/" + symbol + "/" + str(amountInUSD) + "?amountInUSD=true"
        resp = put(url)
        if resp.status_code == 200:
            self.portfolio = resp.json()["portfolio"]
            return self.portfolio
        else:
            raise ValueError("could not sell %s.errorcode: %s, errormessage: %s" % (symbol, str(resp.status_code), str(resp.text)))

    def emergencyLiquidate(self, accountname):
        url = self.url + "emergencyLiquidate/" + accountname
        resp = put(url)
        if resp.status_code == 200:
            self.portfolio = resp.json()["portfolio"]
            return self.portfolio
        else:
            raise ValueError("could not emergency liquidate %s.errorcode: %s, errormessage: %s" % (symbol, str(resp.status_code), str(resp.text)))

    # data get functions
    def getData(self, symbol, lookback = 1):
        # lookback is in days
        url = self.url + "data/priceHistoric/" + symbol + "/" + str(lookback)
        data = get(url).json()
        data = pd.DataFrame(data)
        # it is reversed, so switch around
        data = data.iloc[::-1]
        return data

    def getApeWisdomSymbol(self, symbol, lookback):
        url = self.url + "data/apewisdom/" + symbol + "/" + str(lookback)
        return get(url).json()

    def getApeWisdomLast(self):
        url = self.url + "data/apewisdom/"
        return get(url).json()

    def getFearGreedIndex(self, lookbackdays = 1):
        url = self.url + "data/feargreedindex/" + str(lookbackdays)
        return get(url).json()

    def getBinanceRecentTrades(self, symbol, lookbackdays = -1):
        # -1 means all the data we have
        url = self.url + "data/binancerecenttrades/" + symbol + "/" + str(lookbackdays)
        data = get(url).json()
        data = pd.DataFrame(data)
        return data

    def getTARecommendation(self, symbol):
        url = self.url + "data/tasummary/" + symbol + "/1"
        data = get(url).json()
        if len(data) > 0:
            return data[0]["recommendation"]
        else:
            return None