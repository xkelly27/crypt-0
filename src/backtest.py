# -------- in progress --------


class Backtest:
    def __init__(self, data, start_time, end_time):
        self.data = data
        self.start_time = start_time
        self.end_time = end_time

    def check_data(self):
        return self.data.head()

    def start_of_period_sim(self, initial_investment=1):
        # simulate start of period of data input, add observation at t + 1
        pass

