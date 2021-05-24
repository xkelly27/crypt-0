# meta
from src import data, backtest, plot, stats


# -------------------- acceptable inputs below --------------------

crypto_list = ["BTC-USD", "ETH-USD", "DOGE-USD"]
periods = ["1d", "5d", "1mo", "3mo", "6mo", "1y",
           "2y", "5y", "10y", "ytd", "max"]
intervals = ["1m", "2m", "5m", "15m", "30m", "60m", "90m",
             "1h", "1d", "5d", "1wk", "1mo", "3mo"]
main_setup = {"period": "1mo",
              "interval": "60m"}


def main():
    output_dict = {}
    for crypto in crypto_list:
        df = data.Data(crypto, period=main_setup["period"],
                       interval=main_setup["interval"])
        bds = stats.norm_dict(data=df)["bounds"]
        output_dict[crypto] = stats.is_latest_extreme(data=df, bounds=bds)
    return output_dict


if __name__ == "__main__":
    crypto_data = main()
    for key, val in crypto_data.items():
        if val=="True":
            print(key, val)
        else:
            print("No Moves with selected parameters")