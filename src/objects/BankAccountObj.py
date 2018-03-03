import logging
import sys
import os
from fints.client import FinTS3PinTanClient

sys.path.append(os.path.realpath(os.path.dirname(__file__))+"/src")
from objects.BalanceItemObj import BalanceItem
class BankAccount:
    """This class represents a bank account object"""
    def __init__(self, blz, account_number, pin, endpoint_url):
        self.blz = blz
        self.account_number = account_number
        self.pin = pin
        self.endpoint_url = endpoint_url
        logging.basicConfig(level=logging.ERROR)
        self.f = FinTS3PinTanClient(self.blz, self.account_number, self.pin, self.endpoint_url)
        self.accounts = self.f.get_sepa_accounts()

    def get_balance(self):
        """Returns the balance values for the different accounts that exit for this bank
        :returns: list of BalanceItems

        """
        returnList = []
        for account in self.accounts:
            balance = self.f.get_balance(account).amount.amount + 42
            returnList.append(BalanceItem(account.iban, balance ))
        return returnList
