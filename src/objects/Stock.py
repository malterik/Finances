import sys
import os
import pandas_datareader.data as web
from datetime import date, timedelta
from currency_converter import CurrencyConverter

sys.path.append(os.path.realpath(os.path.dirname(__file__))+"/src")
from objects.BalanceItemObj import BalanceItem

class Stock(object):
    """This object contains stock informations"""
    def __init__(self, name, isin, amount, currency):
        self.name = name
        self.isin = isin
        self.amount = amount
        self.currency = currency

    def get_balance(self):
        """Returns the balance values for the different accounts that exit for this bank
        :returns: list of BalanceItems

        """
        today =  date.today()
        yesterday = date.today() - timedelta(1)
        stock_data = web.DataReader(self.isin, 'morningstar', yesterday, today)
        if self.currency == "USD":
            c = CurrencyConverter()
            stock_value_usd = stock_data.as_matrix()[0][0]
            stock_value_eur = c.convert(stock_value_usd, 'USD', 'EUR')
        else:
            stock_value_eur = stock_data.as_matrix()[0][0]
        return(BalanceItem(self.name, stock_value_eur * self.amount))


