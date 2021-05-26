# meta
from src import data, backtest, plot, stats
import json

# -------------------- see input_data folder for acceptable inputs --------------------

# todo - fix with... open for intervals and periods

def main():
    output_dict = {}

    with open('/input_data/tickers.json') as tickers:
        t = json.load(tickers)
        for crypto in t.values():
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