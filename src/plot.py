import matplotlib.pyplot as plt
import datetime
from scipy.stats import norm
import numpy as np

# meta
from src import stats, data


class Plot:

    # data must be dict from meta "data" module

    def __init__(self, crypto_data: dict):

        if not isinstance(data, dict):
            raise TypeError

        self.data = crypto_data.get("data")
        self.currency = crypto_data.get("currency")
        self.period = crypto_data.get("period")
        self.interval = crypto_data.get("interval")

    def plot(self, kind="price"):
        timestamp = datetime.datetime.now().replace(microsecond=0)
        title = '{} | period: {} | interval: {} | fetched at: {}'.format(self.currency,
                                                                         self.period,
                                                                         self.interval,
                                                                         timestamp)
        fig = plt.figure()
        ax = fig.add_subplot(111)

        if kind == "price":
            close = self.data["Close"]

            ax.plot(close, color='lightgreen')
            ax.set_facecolor('xkcd:white')
            ax.grid(color='lightgrey')

            plt.ylabel('Close Price')
            plt.xlabel('Date')
            plt.suptitle(title)
            plt.show()

        elif kind == "hist" or kind == "histogram":
            pct_change = self.data["pct_change"]

            norm_dict = stats.norm_dict(pct_change)
            bounds = norm_dict.get("bounds")

            std = norm_dict.get("std")
            mu = norm_dict.get("mu")

            domain = np.linspace(np.min(pct_change), np.max(pct_change), 100)
            plt.plot(domain, norm.pdf(domain, mu, std))

            ax.hist(pct_change, bins=40, density=True, alpha=0.6, color='lightgreen')
            ax.set_facecolor('white')
            ax.grid(color='lightgrey')

            plt.axvline(x=bounds[0], color='r')
            plt.axvline(x=bounds[1], color='r')
            plt.axvline(x=mu, color='yellow')

            plt.ylabel('Frequency')
            plt.xlabel('% Change')
            plt.suptitle(title)
            plt.show()

        elif kind == "returns" or kind == "change":
            pct_change = self.data["pct_change"]

            ax.plot(pct_change, color='lightgreen')
            ax.set_facecolor('xkcd:white')
            ax.grid(color='lightgrey')

            plt.ylabel('% Change')
            plt.xlabel('Date')
            plt.suptitle(title)
            plt.show()

