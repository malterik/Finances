class BalanceItem(object):
    """This is an object that includes a descrition and balance"""
    def __init__(self, description, balance):
        self.description = description
        self.balance = float(balance)
    def __str__(self):
        return(self.description + ": " + '%.2f' % self.balance + "€")
