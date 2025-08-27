import pandas as pd

class stock_price(object):

    """
    class for managing the eod historical data for a ticker
    """

    def __init__(self, ticker):
        self.ticker = ticker
        self.hd = pd.DataFrame(colums=["date", "open"])

    def add_price(self, date, value):
        # check of data for the date has not already been saved
        self.hd.loc[-1] = [ date, value ]

    def __str__(self):
        ret_str = self.ticker + "\n"
        ret_str += self.hd + ""