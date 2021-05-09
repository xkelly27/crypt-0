import c_data as CD

# -------- in progress --------

class Backtest:
    def __init__(self, ticker):
        self.data = CD.Data(ticker).get_data()

    def check_data(self):
        return self.data

    def start_of_period_sim(self, initial_investment=1):
        # simulate start of period of data input, add observation at t + 1
        pass

    # need f(x) s.t midpoint is found
    def binary_search(self, array, value, slice=2, offset=0):
        mid = array.length / slice

        pass
