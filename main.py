import c_data as CD
# from .algo import c_backtest as CB


periods = ["1d", "5d", "1mo", "3mo", "6mo", "1y",
           "2y", "5y", "10y", "ytd", "max"]
intervals = ["1m", "2m", "5m", "15m", "30m", "60m", "90m",
            "1h", "1d", "5d", "1wk", "1mo", "3mo"]

crypto_list = ["BTC-USD", "ETH-USD", "DOGE-USD"]


latest = CD.Data(crypto_list[0]).get_latest()
print(latest)



