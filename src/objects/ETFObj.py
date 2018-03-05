
import sys
import os

from lxml import html
import requests

sys.path.append(os.path.realpath(os.path.dirname(__file__))+"/src")
from objects.BalanceItemObj import BalanceItem

class ETF(object):
    """This class contains gold information"""
    def __init__(self, name, amount, url, xpath):
        self.name = name
        self.amount = amount
        self. url = url
        self.xpath = xpath
    def get_balance(self):
        """Returns the balance values for the different accounts that exit for this bank
        :returns: list of BalanceItems

        """
        page = requests.get(self.url)
        tree = html.fromstring(page.content)
        stock_price_str  = tree.xpath(self.xpath)[0].text
        stock_price_str = stock_price_str.replace('EUR', '')
        stock_price =  float(stock_price_str.replace(',', '.'))
        return(BalanceItem(self.name, self.amount * stock_price))
