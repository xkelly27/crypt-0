import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import datetime


class Data:
    def __init__(self, ticker, period="1d", interval="1m"):
        self.ticker = ticker
        self.period = period
        self.interval = interval

    def get_data(self):
        data = yf.download(tickers=self.ticker,
                           period=self.period,
                           interval=self.interval)
        data["pct_change"] = data["Close"].pct_change()
        return data[["Close", "pct_change"]]

    # ------- assert extreme movements ---------

    def norm_dict(self, sig_factor=6):
        # construct norm
        data = self.get_data()["pct_change"]
        std = np.std(data, ddof=1)
        mu = np.mean(data)

        lower = mu - std * sig_factor / 2
        upper = mu + std * sig_factor / 2
        return {"bounds": [lower, upper], "mu": mu, "std": std}

    def is_latest_extreme(self):
        bounds = self.norm_dict().get("bounds")
        latest = self.get_data()[-1]
        if latest < bounds[0] or latest > bounds[1]:
            return True
        else:
            return False

    # -------------------- plot stuff -------------------------

    def plot(self, kind="price"):
        timestamp = datetime.datetime.now().replace(microsecond=0)
        title = '{} | period: {} | interval: {} | fetched at: {}'.format(self.ticker,
                                                                         self.period,
                                                                         self.interval,
                                                                         timestamp)
        fig = plt.figure()
        ax = fig.add_subplot(111)

        data = self.get_data()

        if kind == "price":
            close = data["Close"]

            ax.plot(close, color='lightgreen')
            ax.set_facecolor('xkcd:white')
            ax.grid(color='lightgrey')

            plt.ylabel('Close Price')
            plt.xlabel('Date')
            plt.suptitle(title)
            plt.show()

        elif kind == "hist" or kind == "histogram":
            data = data["pct_change"]

            norm_dict = self.norm_dict()

            std = norm_dict.get("std")
            mu = norm_dict.get("mu")

            domain = np.linspace(np.min(data), np.max(data), 100)
            plt.plot(domain, norm.pdf(domain, mu, std))

            ax.hist(data, bins=40, density=True, alpha=0.6, color='lightgreen')
            ax.set_facecolor('white')
            ax.grid(color='lightgrey')

            bounds = norm_dict.get("bounds")

            plt.axvline(x=bounds[0], color='r')
            plt.axvline(x=bounds[1], color='r')
            plt.axvline(x=mu, color='yellow')

            plt.ylabel('Frequency')
            plt.xlabel('% Change')
            plt.suptitle(title)
            plt.show()

        elif kind == "returns" or kind == "change":
            data = data["pct_change"]

            ax.plot(data, color='lightgreen')
            ax.set_facecolor('xkcd:white')
            ax.grid(color='lightgrey')

            plt.ylabel('% Change')
            plt.xlabel('Date')
            plt.suptitle(title)
            plt.show()