# This module contains a class Wallet that can be used to store, spend, and earn cash.


class Wallet:
    """A wallet that can store, spend, and earn cash.

    Parameters
    ----------
    balance : number
        Amount of starting cash.

    Attributes
    ----------
    item : str
        The type of item, a "Wallet"
    balance : float
        The amount of money currently in the wallet.
    """

    item = "Wallet"

    def __init__(self, balance):
        """See help(Wallet)"""
        self.balance = balance

    def buy_item(self, cost, number=1):
        """Spend money and reduce your balance.

        Parameters
        ----------
        cost : number
            cost of the item to buy.
        number : int
            number of items to buy.

        Raises
        ------
        InsufficientCashError
            If you do not have enough money to spend.
        """
        if cost * number <= self.balance:
            self.balance -= cost * number
        else:
            raise InsufficientCashError(
                f"You can't spend ${cost * number} as you only have ${self.balance}."
            )

    def sell_item(self, cost, number=1):
        """Sell items and increase your balance.

        Parameters
        ----------
        cost : number
            cost of the item to buy.
        number : int
            number of items to buy.

        """
        self.balance += cost * number


class InsufficientCashError(Exception):
    """Custom error used when there is insufficient cash for a transaction."""

    pass
