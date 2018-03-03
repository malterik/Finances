#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from datetime import date
from fints.client import FinTS3PinTanClient

sys.path.append(os.path.realpath(os.path.dirname(__file__))+"/src")
from objects.BankAccountObj import BankAccount
from objects.BitcoinObj import Bitcoin
from objects.Stock import Stock
from objects.BalanceItemObj import BalanceItem
from utils.parseData import parseData


items = parseData("./data/")
balance_list = []
for item in items:
    if isinstance(item, BankAccount):
        for balanceItem in item.get_balance():
            balance_list.append(balanceItem)
    elif isinstance(item, Stock):
        balance_list.append(item.get_balance())
    elif isinstance(item, Bitcoin):
        balance_list.append(item.get_balance())
    else:
        print("Unknown instance type")

sum = 0
for balance_item in balance_list:
    sum += balance_item.balance
    print(balance_item)
print(BalanceItem("Total", sum))