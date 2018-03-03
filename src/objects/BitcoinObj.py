
import sys
import os
from exchanges.coinapult import Coinapult

sys.path.append(os.path.realpath(os.path.dirname(__file__))+"/src")
from objects.BalanceItemObj import BalanceItem

class Bitcoin(object):
    """This class contains bitcoin information"""
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def get_balance(self):
        """Returns the balance values for the different accounts that exit for this bank
        :returns: list of BalanceItems

        """
        bitcoin_price = float(Coinapult().get_current_price(currency='EUR'))
        return(BalanceItem(self.name, self.amount * bitcoin_price))
