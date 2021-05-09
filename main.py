# meta
from src import data, backtest, plot, stats


def test():
    periods = ["1d", "5d", "1mo", "3mo", "6mo", "1y",
               "2y", "5y", "10y", "ytd", "max"]
    intervals = ["1m", "2m", "5m", "15m", "30m", "60m", "90m",
                 "1h", "1d", "5d", "1wk", "1mo", "3mo"]

    crypto_list = ["BTC-USD", "ETH-USD", "DOGE-USD"]

    output = []
    for i in crypto_list:
        latest = str(data.Data(i).get_latest())
        output.append(i + " latest -> " + latest)
    print(output)

test()