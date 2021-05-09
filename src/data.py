import yfinance as yf


class Data:

    '''
    yfinance w/ the plug
    note: crypto data UTC!
    '''

    def __init__(self, currency, period="1d", interval="1m"):
        self.currency = currency
        self.period = period
        self.interval = interval

    def get_data(self):
        data = yf.download(tickers=self.currency,
                           period=self.period,
                           interval=self.interval)
        data["pct_change"] = data["Close"].pct_change()
        return {"currency": self.currency, "period": self.period, "interval": self.interval,
                "data": data[["Close", "pct_change"]]}

    def get_latest(self):
        table = self.get_data().get("data")
        data = table["Close"]
        return round(data[-1], 2)