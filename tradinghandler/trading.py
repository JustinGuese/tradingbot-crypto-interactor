from requests import post, get, put

class TradingInteractor():
    def __init__(self, accountname):
        self.url = "http://192.168.178.36:30002/"
        self.accountname = accountname
        self.portfolio = None

    def getPortfolio(self):
        if self.portfolio is None:
            url = self.url + "portfolio/" + self.accountname
            self.portfolio = get(url)
        return self.portfolio

    def getUSD(self):
        if self.portfolio is None:
            self.getPortfolio()
        return self.portfolio["USDT"]

    def getData(self, symbol, lookback = 1):
        # lookback is in days
        url = self.url + "priceHistoric/" + symbol + "/" + str(lookback)
        return get(url)

    def getApeWisdom(self, symbol, lookback):
        url = self.url + "apewisdom/" + symbol + "/" + str(lookback)
        return get(url)

    def buy(self, symbol, amountInUSD):
        url = self.url + "buy/" + self.accountname + "/" + symbol + "/" + str(amountInUSD) + "?amountInUSD=true"
        self.portfolio = put(url)
        return self.portfolio

    def sell(self, symbol, amountInUSD = -1):
        url = self.url + "sell/" + self.accountname + "/" + symbol + "/" + str(amountInUSD) + "?amountInUSD=true"
        self.portfolio = put(url)
        return self.portfolio