
import sys
import os

from lxml import html
import requests

sys.path.append(os.path.realpath(os.path.dirname(__file__))+"/src")
from objects.BalanceItemObj import BalanceItem

class Gold(object):
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
        gold_price_str = tree.xpath(self.xpath)[0].text
        gold_price_str =  gold_price_str.replace('.', '')
        gold_price =  float(gold_price_str.replace(',', '.'))
        return(BalanceItem(self.name, self.amount * gold_price))
