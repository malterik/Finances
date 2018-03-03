import json
from os import listdir
import sys
import os

sys.path.append(os.path.realpath(os.path.dirname(__file__))+"/src")
from objects.BankAccountObj import BankAccount
from objects.Stock import Stock
from objects.BitcoinObj import Bitcoin

def parseData(pathToData):
    """This function parses all the data items in the data folder and generates a list of all the objects

    :pathToData: TODO
    :returns: TODO

    """
    resultList = []
    for f in listdir(pathToData):
        data = json.load(open(pathToData+f))
        if data["Type"] == "BankAccount":
            resultList.append(BankAccount(data["BLZ"], data["AccountNumber"], data["Pin"], data["EndpointURL"]))
        elif data["Type"] == "Stock":
            resultList.append(Stock(data["Name"], data["ISIN"], data["Amount"], data["Currency"]))
        elif data["Type"] == "Bitcoin":
            resultList.append(Bitcoin(data["Name"], data["Amount"]))
        else:
            print(data["Type"])
            raise NameError("Invalid Object Type")
    return resultList
